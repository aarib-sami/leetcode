class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.freqSet = {}
        for n in self.nums:
            self.freqSet[n] = 1 + self.freqSet.get(n, 0)

    def showFirstUnique(self) -> int:
        for n in self.nums:
            if self.freqSet[n] < 2:
                return n
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.freqSet[value] = 1 + self.freqSet.get(value, 0)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)