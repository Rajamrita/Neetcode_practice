from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # Attach the remaining nodes
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


# Helper function to create a linked list
def createList(values):
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


# Helper function to print a linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Main Program
list1 = createList([1, 3, 5])
list2 = createList([2, 4, 6])

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

print("Merged List:")
printList(merged)