"""

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:



"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        num = 0

        while x > 0:
            digit = x % 10
            num = num * 10 + digit
            x = x // 10

        if  temp == num:
            return "true"
        else:
            return "false"

obj = Solution()    
print(obj.isPalindrome(121))