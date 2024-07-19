class Solution:
    def myAtoi(self, s: str) -> int:
        string=s.strip()
        if not string:
            return 0
        number,idx,sign=0,0,1
        MIN_INT,MAX_INT=-2**31,2**31-1
        
        if string[0]=="+" or string[0]=="-":
            sign*=1 if string[0]=="+" else -1
            idx+=1
        
        while idx<len(string) and string[idx].isdigit():
            digit=int(string[idx])
            if number > (MAX_INT-digit)//10:
                return MAX_INT if sign==1 else MIN_INT
            number=number*10+digit
            idx+=1

        return sign*number