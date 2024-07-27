class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr=[]
        if not digits:
            return arr
        letter_no={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def backtrack(combination,next_digits):
            if not next_digits:
                return arr.append(combination)
            
            for letter in letter_no[next_digits[0]]:
                backtrack(combination+letter,next_digits[1:])
        backtrack("",digits)
        return arr