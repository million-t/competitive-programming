def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return 1
    return 0
