class CRUD():

    def __init__(self):
        self.tasks = []

    # create task
    def add(self, todo):
        self.tasks.append({"task": todo, "done": False})
        return self.tasks

        # create task
    def add(self, todo):
        self.tasks.append({"task": todo, "done": False})
        return self.tasks

    # read task
    def show(self):
        return self.tasks

    # delete task
    def delete(self, index):
        del self.tasks[index]
        return self.tasks

    # mark is done/undone
    def check(self, index):
        self.tasks[index]['done'] = not self.tasks[index]['done']
        return self.tasks
