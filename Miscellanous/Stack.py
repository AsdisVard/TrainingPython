__author__ = 'asdis'

class Stack:
    table = []
    def push(self):
        flag = True
        while flag == True:
            print("Gimme number or press 'x' to quit: ")
            a = input()
            if a == 'x':
                flag = False
            else:
                self.table.append(a)
        print(self.table)
    def pop(self):
        if self.table.__len__ == 0:
            print("There is no record in the requested list")
        else:
            print(self.table.pop())

stack = Stack()
stack.push()

var = stack.pop()
print(var)