class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=list(zip(*strs))
        print(l)
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

        #longest common prefix 31 ms
