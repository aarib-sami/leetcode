# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        ptr = res

        while l1 or l2 or carry:
            ptr.next = ListNode()
            ptr = ptr.next
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sum = v1 + v2 + carry

            carry = sum // 10
            val = sum % 10

            ptr.val = val
            
            

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next