class Solution:
    def checkDivisibility(self, n: int) -> bool:
        div=[]
        start=n
        while n!=0:
            div.append(n%10)
            n=int(n/10)
        s=0
        p=1
        for i in div:
            s=s+i
            p=p*i
        return True if (start%(s+p))==0 else False