import singly_linked_list as ll

def find_middle(head):
    """
    :type head: singly_linked_list.Node
    """
    slow = head
    fast = head.nextt.nextt

    while fast and fast.nextt:
        fast = fast.nextt.nextt
        slow = slow.nextt

    return slow

if __name__ == "__main__":
    l = range(2,9)
    sll = ll.SinglyLinkedList()
    head = sll.create_singly_linked_list(l)

    #debug
    sll.print_list();

    middle = find_middle(head)

    # if not middle:
    #     print "None"
    # else:
    #     print str(middle.data)
    print middle.data if middle else "None"

