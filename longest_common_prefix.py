"""
str = ["flower" , "flight" , "flying"]
output = "fl"


"""

"""
str = ["flower" , "flight" , "flying"]
output = "fl"


"""

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]

        for i in range(len(base)):
            for word in strs[1:]:
                if  base[i] != word[i]:
                    return base[:i]

        return base

strs = ["flower" , "flight" , "flying"]
obj = Solution()
print(obj.longestCommonPrefix(strs))
