class Stack:

    def __init__(self):
        self.lis = []

    def is_empty(self):
        return self.lis == []

    def push(self, object):
        self.lis.append(object)

    def pop(self):
        return self.lis.pop()

    def peek(self):
        try:
            return self.lis[len(self.lis) - 1]
        except IndexError:
            return ''

    def size(self):
        return len(self.lis)