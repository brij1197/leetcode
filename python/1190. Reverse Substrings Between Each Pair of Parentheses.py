class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[""]
        for char in s:
            if char not in "()":
                stack[-1]+=char
            elif char=="(":
                stack.append("")
            else:
                rev=stack.pop()[::-1]
                stack[-1]+=rev
        return "".join(stack)