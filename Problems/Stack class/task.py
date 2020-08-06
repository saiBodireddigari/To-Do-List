class Stack():

    def __init__(self):
        self.table = []

    def push(self, el):
        return self.table.append(el)

    def pop(self):
        return self.table.pop(-1)

    def peek(self):
        return self.table[-1]

    def is_empty(self):
        if not self.table:
            return True
        return False
