class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue

            anagram = []

            for j in range(len(strs)):
                if not visited[j] and sorted(strs[j]) == sorted(strs[i]):
                    anagram.append(strs[j])
                    visited[j] = True

            result.append(anagram)

        return result