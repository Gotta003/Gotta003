class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        num_float: List[float]=[]
        q1=0
        q2=0
        for idx, i in enumerate(num):
            if i=='?':
                val=0
                if idx<n//2:
                    q1+=1
                else:
                    q2+=1
            else:
                val=float(i)
            num_float.append(val)
        left_values=sum(num_float[0:n//2])
        right_values=sum(num_float[n//2:n])
        if(q1+q2)%2==1:
            return True
        return (left_values-right_values)*2!=9*(q2-q1)