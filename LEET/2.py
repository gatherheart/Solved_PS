# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        carry, remain = 0, 0

        while l1 or l2:
            remain = (l1.val + l2.val) % 10
            carry = (l1.val + l2.val) // 10
            l3.val += remain
            l3.next = ListNode(val=carry)

            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        return l3
