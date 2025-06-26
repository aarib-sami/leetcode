class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        curSet = []
        curSum = 0

        def dfs(i, curSum):
            if i >= len(candidates) or curSum > target:
                return 
            elif curSum == target:
                res.append(curSet.copy())
                return

            curSet.append(candidates[i])
            curSum += candidates[i]
            dfs(i, curSum)

            curSet.pop()
            curSum -= candidates[i]
            dfs(i+1, curSum)

        dfs(0, 0)
        return res