class Node:
    def __init__(self, val, nextt=None):
        self.data = val
        self.nextt = nextt

class SinglyLinkedList:

    def __init__(self, val=None):
        self.head = None if val is None else Node(val)
    def create_singly_linked_list(self, list):

        prev = None
        for c in list:
            new_node = Node(c)
            if self.head is None:
                self.head = new_node
                prev = self.head
            else:
                prev.nextt = new_node
                prev = new_node

        return self.head

    def print_list(self, head=None):
        if head is None:
            curr = self.head
        else:
            curr = head
        while curr:
            print str(curr.data) + " ",
            curr = curr.nextt
        print

    def push(self, val):
        new_node = Node(val)
        new_node.nextt = self.head
        self.head = new_node

if __name__ == "__main__":
    l = range(2,9)
    sll = SinglyLinkedList()
    head = sll.create_singly_linked_list(l)
    sll.print_list()

    sll2 = SinglyLinkedList()
    sll2.push(5)
    sll2.push(4)
    sll2.push(3)
    sll2.push(2)
    sll2.push(1)

    sll2.print_list()
