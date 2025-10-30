class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        i = 0
        while True:
            if i>= len(strs[0]):
                break
            c = strs[0][i]
            for string in strs:
                if i>=len(string) or string[i] != c:
                    return r
            r +=c
            i+=1
        return r                
        
