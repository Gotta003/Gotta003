class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        #Remove multiples
        coins=sorted(list(set(coins)))
        r_coins=[]
        for c in coins:
            if not any(c%smaller==0 for smaller in r_coins):
                r_coins.append(c)
        coins=r_coins
        #LCMs
        lcm_subsets=[]
        n=len(coins)
        for size in range(1, n+1):
            for comb in combinations(coins, size):
                current_lcm=1
                for val in comb:
                    current_lcm=math.lcm(current_lcm, val)
                sign=1 if size%2==1 else -1
                lcm_subsets.append((current_lcm, sign))
        #Binary Search
        def count_multiples(x):
            total=0
            for l, sign in lcm_subsets:
                total+=sign*(x//l)
            return total

        low=min(coins)
        high=min(coins)*k
        ans=high
        while low<=high:
            mid=(low+high)//2
            if count_multiples(mid)>=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans