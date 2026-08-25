class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        val=k
        for i in nums:
            if val==i:
                val+=k
        return val