class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        curSum = 0
        candidates.sort()

        def dfs(i, curSum):
            if curSum == target:
                res.append(subset.copy())
                return
            elif i >= len(candidates) or curSum > target:
                return
            subset.append(candidates[i])
            curSum += candidates[i]
            dfs(i+1, curSum)

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            curSum -= candidates[i]
            dfs(i+1, curSum)
        
        dfs(0, 0)
        return res