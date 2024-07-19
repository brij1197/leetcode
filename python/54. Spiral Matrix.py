class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        result=[]
        while top<=bottom and left<=right:
            for idx in range(left,right+1):
                result.append(matrix[top][idx])
            top+=1
            
            for idx in range(top,bottom+1):
                result.append(matrix[idx][right])
            right-=1
            
            if top<=bottom:
                for idx in range(right,left-1,-1):
                    result.append(matrix[bottom][idx])
            bottom-=1
            
            if left<=right:
                for idx in range(bottom,top-1,-1):
                    result.append(matrix[idx][left])
            left+=1
        return result