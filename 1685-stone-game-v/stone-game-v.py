class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n: int=len(stoneValue)
        if n<=1:
            return 0
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+stoneValue[i]
        print(prefix)
        #dp[i, j]= max point of stoneValue[i...j]
        dp=[[0]*n for _ in range(n)]
        max_left=[[0]*n for _ in range(n)]
        max_right=[[0]*n for _ in range(n)]
        for i in range(n):
            max_left[i][i]=stoneValue[i]
            max_right[i][i]=stoneValue[i]

        def get_sum(i: int, j: int):
            return prefix[j+1]-prefix[i]

        #Substringg at least 2 and max n
        for length in range(2, n+1):
            k=0
            for i in range(n-length+1):
                j=i+length-1
                # Taglio
                if k<i:
                    k=i
                while (k<j and get_sum(i,k)*2<get_sum(i,j)):
                    k+=1
                ans=0
                if get_sum(i, k)*2==get_sum(i, j):
                    left_part=max_left[i][k]
                    right_part=max_right[k+1][j]
                    ans=max(left_part, right_part)
                    if k-1>=i:
                        ans=max(ans, max_left[i][k-1])
                    if k+2<=j:
                        ans=max(ans, max_right[k+2][j])
                else:
                    if k-1>=i:
                        ans=max(ans, max_left[i][k-1])
                    if k+1<=j:
                        ans=max(ans, max_right[k+1][j])
                dp[i][j]=ans
                max_left[i][j]=max(max_left[i][j-1], ans+get_sum(i, j))
                max_right[i][j]=max(max_right[i+1][j], ans+get_sum(i, j))
        return dp[0][n-1]