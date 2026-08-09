'''
Runtime: 0ms (Beats 100%)
Memory: 19.24MB (Beats 52.48%)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        No. ways to get to step n = (no. ways step n-1) + (no. ways step n-2) 
        
        Since you can only take 1 step or 2 step at once, there's only 1 way to get to n from n-1, and 1 way to get to n from n-2. Thus, the number of ways to get to n is the number of ways to get there from n-2 and n-1.

        Uses top-down with memoization to cache overlapping sub-problems so we don't have to recalculate it very time.

        '''
        memo = {}
        memo[1] = 1 
        memo[2] = 2

        if (n==0): return 0
        if (n==1): return 1
        if (n==2): return 2

        def climb(n):
            if (n in memo.keys()):
                return memo[n]
            curr = climb(n-1) + climb(n-2)
            memo[n] = curr
            return curr
        
        return climb(n)