class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqToVal = defaultdict(list)
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        for val, freq in counter.items():
            freqToVal[freq].append(val)

        res = []

        for i in range(len(nums), -1, -1):
            if i not in freqToVal:
                continue
            for j in freqToVal[i]:
                res.append(j)
                k -= 1
                if k == 0: return res