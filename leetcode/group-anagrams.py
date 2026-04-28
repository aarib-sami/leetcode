class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupSet = defaultdict(list)

        for s in strs:
            letterCount = [0] * 26
            for c in s:
                letterCount[ord(c) - ord('a')] += 1
            groupSet[tuple(letterCount)].append(s)

        res = []

        for group in groupSet.values():
            res.append(group)

        return res