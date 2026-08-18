class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n: int=len(nums)
        if k==n:
            return max(nums)
        map_nums: dict[int, int]={}
        for i in nums:
            map_nums[i]=0
        for offset in range(n-k+1):
            for length in range(k):
                idx=offset+length
                map_nums[nums[idx]]+=1
        z=-1
        for x, y in map_nums.items():
            if y==1 and x>z:
                z=x
        return z