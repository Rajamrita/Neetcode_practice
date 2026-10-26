from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: Merge both halves
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2


# Helper function: create linked list
def createList(values):
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


# Helper function: print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Main Program
head = createList([1, 2, 3, 4, 5])

solution = Solution()
solution.reorderList(head)

print("Reordered List:")
printList(head)