from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {t.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for t in self.tasks:
            if t.completed:
                counter += 1
                self.tasks.remove(t)
        return f"Cleared {counter} tasks."

    def view_section(self):
        view_list = []
        view_list.append(f"Section {self.name}:")
        for n in self.tasks:
            view_list.append(n.details())
        return '\n'.join(view_list)






