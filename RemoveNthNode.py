class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Step 1: Move right pointer n steps forward
        for _ in range(n):
            right = right.next

        # Step 2: Move both pointers together
        while right:
            left = left.next
            right = right.next

        # Step 3: Remove the required node
        left.next = left.next.next

        return dummy.next


# Convert a list into a linked list
def createLinkedList(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Print the linked list
def printLinkedList(head):
    values = []

    while head:
        values.append(str(head.val))
        head = head.next

    print(" -> ".join(values))


# Main program
head = createLinkedList([1, 2, 3, 4, 5])
n = 2

solution = Solution()
head = solution.removeNthFromEnd(head, n)

print("After removing the nth node from the end:")
printLinkedList(head)