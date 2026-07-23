class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={'{':'}','[':']','(':')'}


        for ch in s:
            if ch in d:
                stack.append(d[ch])
            else:
                if not stack or stack[-1]!=ch:
                    return False
                stack.pop()
        if len(stack)==0:
            return True
        return False
        