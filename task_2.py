class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    head.next = swap_pairs(head.next.next)
    new_head.next = head
    return new_head


def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Input:")
print_linked_list(head)

result = swap_pairs(head)
print("\nOutput:")
print_linked_list(result)
