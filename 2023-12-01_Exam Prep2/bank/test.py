from project.bank_app import StudentLoan
from project.loans.mortgage_loan import MortgageLoan

loan_type = "StudentLoan"

VALID_LOAN_TYPES = {
    "StudentLoan": StudentLoan,
    "MortgageLoan": MortgageLoan
}

list = [StudentLoan, MortgageLoan, StudentLoan, MortgageLoan]
list.remove(VALID_LOAN_TYPES[loan_type])
print(list)

