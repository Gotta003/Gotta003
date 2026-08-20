class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        x1=nums[0]
        x2=nums[1]
        n=len(nums)
        a1=[x1]
        a2=[x2]
        for i in range(2, n):
            if x1>x2:
                x1=nums[i]
                a1.append(x1)
            else:
                x2=nums[i]
                a2.append(x2)
        a_s=a1+a2
        return a_s      