class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arraySum = sum(nums)
        if arraySum % 2 != 0: return False
        
        target = arraySum / 2
        sumSet = set()

        for n in nums:
            if not sumSet:
                sumSet.add(n)
            else:
                vals = []
                for s in sumSet:
                    vals.append(s+n)
                
                for v in vals:
                    sumSet.add(v)
            
            if target in sumSet:
                return True


        return False