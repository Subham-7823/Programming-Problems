"""
leetcode 13
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation:M = 1000, CM = 900, XC = 90 and IV = 4.

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = dict[s[-1]]
        
        for i in range(len(s)-2,-1,-1):
            if dict[s[i]]<dict[s[i+1]]:
                result = result - dict[s[i]]
            else:
                result = result + dict[s[i]]
        return result
obj = Solution()
print(obj.romanToInt("VL"))
