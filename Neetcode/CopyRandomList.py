
from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # Step 1: Create copies of all nodes
        old_to_copy = {None: None}

        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Assign next and random pointers
        curr = head
        while curr:
            copy = old_to_copy[curr]

            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]

            curr = curr.next

        return old_to_copy[head]


# Helper function to print the linked list
def printList(head):
    curr = head

    while curr:
        random_value = curr.random.val if curr.random else None
        print(f"Value: {curr.val}, Random: {random_value}")
        curr = curr.next


# Main Program
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

# Connect next pointers
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Connect random pointers
node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

solution = Solution()
copied_head = solution.copyRandomList(node1)

print("Copied Linked List:")
printList(copied_head)
