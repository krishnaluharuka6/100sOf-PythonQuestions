# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common = ""
        x=0
        iterate = len(strs[0])
        for k in range(iterate):
            for i,str in enumerate(strs):
                if(i == len(strs)-1):
                    break
                else:
                    next = strs[i+1]
                if(str[x] == next[x] and i == len(strs)-2):
                    common += str[x]
                    x += 1
                elif(str[x] != next[x]):
                    return common
        return common


            
        # return common


s = Solution()
result = s.longestCommonPrefix(["c"])
print(f"Common longest prefix is '{result}'")



#optimal
class Solution:
    def longestCommonPrefix(self, v) -> str:
        common = ""
        v=sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i] != last [i]):
                return common
            common += first[i]
        return common
sol = Solution()
result = sol.longestCommonPrefix(["aaa","aa","aaa"])
print(f"Common longest prefix is '{result}'")