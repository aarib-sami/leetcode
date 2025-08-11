class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.leftPointer, self.rightPointer = ListNode(0), ListNode(0)
        self.leftPointer.right, self.rightPointer.left = self.rightPointer, self.leftPointer
        self.capacity = 0
        self.maxCapacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        aheadNode = self.leftPointer.right
        
        node = ListNode(value)
        node.left = self.leftPointer
        node.right = aheadNode

        aheadNode.left = node

        self.leftPointer.right = node
        
        self.capacity += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        secondLast = self.rightPointer.left.left
        secondLast.right = self.rightPointer
        self.rightPointer.left = secondLast

        self.capacity -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.rightPointer.left.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.leftPointer.right.val

    def isEmpty(self) -> bool:
        return self.capacity == 0

    def isFull(self) -> bool:
        return self.capacity == self.maxCapacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()