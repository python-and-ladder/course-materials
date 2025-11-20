class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next:
            return f"[{self.data}]->{repr(self.next)}"
        return f"[{self.data}]"

class LinkedList:
    pass

a = LLNode(1)
b = LLNode(2)
c = LLNode(3)
a.next = b
b.next = c
print(b)