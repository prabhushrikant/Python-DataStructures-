import singly_linked_list as ll

def getTail(head):

    while head.nextt is not None:
        head = head.nextt

    return head

# reverse only part of the linked list starting from
# given start and end node
# and return new head & tail
def reverse(start, end):
    prev = None
    tail = start
    temp = None if end is None else end.nextt
    while start != temp:
        nextt = start.nextt

        start.nextt = prev

        prev = start
        start = nextt

    return prev, tail


# iterative approach
def reverse_in_group(head, k):
    # Code here
    prev = None
    fast = head
    new_head = None
    prev_tail = None
    while fast is not None:
        slow = fast
        # increment fast pointer by k
        i = 1
        while fast is not None and i < k:
            fast = fast.nextt
            i += 1

        # store fast.next for future use.
        # if fast is None or fast.nextt is None:
        #     temp = fast
        # else:
        temp = None if fast is None else fast.nextt

        head, tail = reverse(slow, fast)
        if prev_tail is None:
            prev_tail = tail
        else:
            prev_tail.nextt = head
            prev_tail = tail
        if new_head is None:
            new_head = head
        fast = temp
    return new_head

def reverse_in_group_recursive(head, k):

     temp = head

     if temp is None:
         return
     else:

         #store next node to be processed in temp
         i = 0
         while temp is not None and i < k:
            temp = temp.nextt
            i += 1

         # reverse the linklist
         i = 0
         prev = None
         next = None
         curr = head

         while curr is not None and i < k:
             next = curr.nextt

             curr.nextt = prev

             prev = curr
             curr = next
             i += 1

         head.nextt = reverse_in_group_recursive(temp, k)

         return prev


if __name__ == "__main__":
    l = range(1,6)
    sll = ll.SinglyLinkedList()
    head = sll.create_singly_linked_list(l)
    sll.print_list()

    # new_head = reverse_in_group(head, 3)

    new_head = reverse_in_group_recursive(head, 2)
    # printing the reversed list.
    sll.print_list(new_head)