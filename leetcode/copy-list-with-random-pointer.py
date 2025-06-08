"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copyHead = None
        copyMap = {None: None}

        ptr = head
        while ptr:
            copyMap[ptr] = Node(ptr.val)
            ptr = ptr.next

        ptr = head
        while ptr:
            copy = copyMap[ptr]
            copy.next = copyMap[ptr.next]
            copy.random = copyMap[ptr.random]
            copyMap[ptr] = copy
            ptr = ptr.next

        return copyMap[head]