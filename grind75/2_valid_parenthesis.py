# https://leetcode.com/problems/valid-parentheses/
# https://www.youtube.com/watch?v=WTzjTskDFMg&list=PLF_1Qi3jFDOsicefz1oRwhjPsKHdOD0A0&index=2

# Time O(n) -> iterating only once , Space O(n) -> Max stack size = max len of string


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenMapping = {"]": "[", ")": "(", "}": "{"}

        for char in s:
            if char in closeToOpenMapping:
                if stack and stack[-1] == closeToOpenMapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


string = s = "()[]{}"
s = Solution()
print(s.isValid(string))
