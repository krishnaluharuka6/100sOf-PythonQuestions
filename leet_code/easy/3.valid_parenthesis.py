class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        prev = ""
        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
            elif i == "}":
                if(stack == []):
                    return False
                prev = stack.pop()
                if prev != "{" :
                    return False
            elif i == "]":
                if(stack == []):
                    return False
                prev = stack.pop()
                if prev != "[" or prev == "":
                    return False
            elif i == ")":
                if(stack == []):
                    return False
                prev = stack.pop()
                if prev != "(" or prev == " ":
                    return False
        if stack == []:
            return True
        else:
            return False
    

sol = Solution()
result = sol.isValid("([)]")
print(result)
