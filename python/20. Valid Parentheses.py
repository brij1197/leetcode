class Solution:
    def isValid(self, s: str) -> bool:
        dict_brac={
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack=[]
        
        for i in s:
            if i in dict_brac.values():
                stack.append(i)
            elif i in dict_brac.keys():
                if stack==[] or stack.pop()!=dict_brac[i]:
                    return False
            else:
                return False
        return stack==[]