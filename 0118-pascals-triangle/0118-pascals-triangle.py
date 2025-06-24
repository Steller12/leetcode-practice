class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x=[[1]]
        for i in range(2,numRows+1):
            x.append([1]*i)
        for i in range(2,len(x)):
            for j in range(1,i):
                x[i][j]=x[i-1][j-1]+x[i-1][j]
        return x