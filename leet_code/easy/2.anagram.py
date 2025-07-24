""" Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        # if len(s) != len(t):
        #     return False
        
        # check_s = {

        # }


        # for i in s:
        #     count = s.count(i)
        #     check_s[i] = count

        # for i in t:
        #     if i not in check_s.keys():
        #         return False
        #     else:
        #         check_s[i] -= 1

        # return all(x == 0 for x in check_s.values())


        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
            return False
            
        



sol = Solution()
result = sol.isAnagram("nagaram","anagram")
print(result)


