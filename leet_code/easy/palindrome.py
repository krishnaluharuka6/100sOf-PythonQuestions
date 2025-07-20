# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        if x < 0:
            return False
        else:
            reverse = 0
            while x != 0:
                remainder = x % 10
                x = x // 10
                reverse = reverse*10 + remainder

            if(reverse == y):
                return True 
            else:
                return False

       

s = Solution()
result = s.isPalindrome(121)
print(result)
        