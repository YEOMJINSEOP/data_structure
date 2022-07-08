from ast import main


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, val):
        self.last = Node(val, self.last)

    def pop(self):
        val = self.last.val
        self.last = self.last.next
        return val
