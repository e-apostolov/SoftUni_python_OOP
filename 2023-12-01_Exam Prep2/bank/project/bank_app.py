from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }
    VALID_CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult
    }
    VALID_CLIENT_LOANS = {
        "Student": "StudentLoan",
        "Adult": "MortgageLoan"
    }

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")
        loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."
        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(x for x in self.clients if x.client_id == client_id)
        loan = next(x for x in self.loans if x.__class__.__name__ == loan_type)
        if loan_type != self.VALID_CLIENT_LOANS[client.__class__.__name__]:
            raise Exception("Inappropriate loan type!")
        client.loans.append(loan)
        self.loans.remove(next(x for x in self.loans if x.__class__.__name__ == loan_type))
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        client = next((x for x in self.clients if x.client_id == client_id), None)
        if client not in self.clients:
            raise Exception("No such client!")
        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                l.increase_interest_rate()
                number_of_changed_loans += 1
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        number_of_changed_client_loans = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                number_of_changed_client_loans += 1
        return f"Number of clients affected: {number_of_changed_client_loans}."

    def get_statistics(self):
        sum_interest = sum(x.interest for x in self.clients)
        average_client_interest_rate = sum_interest/len(self.clients) if sum_interest else 0
        return f"Active Clients: {len(self.clients)}\n"\
               f"Total Income: {sum(x.income for x in self.clients):.2f}\n"\
               f"Granted Loans: {sum(len(x.loans) for x in self.clients)}, Total Sum: {sum(sum(y.amount for y in x.loans) for x in self.clients):.2f}\n"\
               f"Available Loans: {len(self.loans)}, Total Sum: {sum(x.amount for x in self.loans):.2f}\n"\
               f"Average Client Interest Rate: {average_client_interest_rate:.2f}"













