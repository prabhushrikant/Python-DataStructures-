# https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1

# method 1 (simple)
#         1. travel the tree in In-Order fashion
#         2. While travelling instead of printing them collect them into a node array
#         3. Travel through node array and convert to the doubly link list.

# method 2 (in place)

import BinaryTree as b_tree

class DLLNode:
    def __init__(self, val, nextt=None, prev=None):
        self.data = val
        self.nextt = nextt
        self.prev = prev

    # we needed this functions because we didn't want to accidently set
    # already set prev pointer when tree returns.
    def set_prev(self, prev=None):
        if self.prev is None:
            self.prev = prev

    # we needed this functions because we didn't want to accidently set
    # already set next pointer when tree returns.
    def set_nextt(self, nextt=None):
        if self.nextt is None:
            self.nextt = nextt

def BTToDLL(root):
    # do Code here
    if root is None:
        return None
    else:
        dll = None #empty node
        dll_head = dll
        dll_front, dll_head = ToDLL(root, dll, dll_head)
        return dll_head

def ToDLL(root, dll, head):
    if root is None:
        return dll, head
    else:
        dll_prev, head = ToDLL(root.left, dll, head)
        dll = DLLNode(root.data)
        if head is None:
            head = dll
            head.prev = None
        if head.nextt is None and head is not dll:
            head.nextt = dll
        if dll_prev is not None and dll_prev != dll:
            dll_prev.set_nextt(dll)
            dll.set_prev(dll_prev)
        dll_next, head = ToDLL(root.right, dll, head)
        if head is None:
            head = dll
            head.prev = None
        if head.nextt is None and head is not dll:
            head.nextt = dll
        if dll_next is not None and dll_next != dll:
            dll_next.set_prev(dll)
            dll.set_nextt(dll_next)

        return dll_next, head


if __name__ == "__main__":

    # example 1

    tree = b_tree.BinaryTree(10)
    root = tree.root
    root.left = b_tree.Node(12)
    root.right = b_tree.Node(15)
    root.left.left = b_tree.Node(25)
    root.left.right = b_tree.Node(30)
    root.right.left = b_tree.Node(36)


    head = BTToDLL(root)

    # print doubly linked list
    while head is not None:
        print str(head.data) + " ",
        head = head.nextt
    print


    # example 2
    # tree = b_tree.BinaryTree(1)
    # root = tree.root
    # root.left = b_tree.Node(2)
    # root.right = b_tree.Node(3)
    #
    # head = BTToDLL(root)
    #
    # # print doubly linked list
    # while head is not None:
    #     print str(head.data) + " ",
    #     head = head.nextt
    # print

    # example 3
    # tree = b_tree.BinaryTree(10)
    # root = tree.root
    # root.left = b_tree.Node(20)
    # root.right = b_tree.Node(30)
    # root.left.left = b_tree.Node(40)
    # root.left.right = b_tree.Node(60)
    #
    # head = BTToDLL(root)
    #
    # # print doubly linked list
    # while head is not None:
    #     print str(head.data) + " ",
    #     head = head.nextt
    # print
