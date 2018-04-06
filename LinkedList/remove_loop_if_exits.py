import singly_linked_list as ll
def remove_loop(head):
    slow = head
    fast = head

    while fast is not None and fast.nextt is not None:
        slow = slow.nextt
        fast = fast.nextt.nextt
        if slow == fast:
            break;

    if fast is None or fast.nextt is None:
        # there is no loop.
        return head

    slow = head
    while slow.nextt != fast.nextt:
        slow = slow.nextt
        fast = fast.nextt

    fast.nextt = None  #removing the loop

    return head



if __name__ == '__main__':

    sll = ll.SinglyLinkedList(1)
    # create linked list with loop
    sll.head.nextt = ll.Node(2)
    sll.head.nextt.nextt = ll.Node(3)
    loop_start = ll.Node(4)
    sll.head.nextt.nextt.nextt = loop_start
    sll.head.nextt.nextt.nextt.nextt = ll.Node(5)
    sll.head.nextt.nextt.nextt.nextt.nextt = ll.Node(6)
    sll.head.nextt.nextt.nextt.nextt.nextt.nextt = ll.Node(7)

    sll.head.nextt.nextt.nextt.nextt.nextt.nextt.nextt = loop_start

    new_head = remove_loop(sll.head)
    sll.print_list(new_head)