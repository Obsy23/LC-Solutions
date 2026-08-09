'''
Runtime: 0ms (Beats 100%)
Memory: 19.29MB (Beats 79.30%)
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        The min cost at stair n is the minimum between the cost at stair n-2, and the stair at n-1.

        Since there's two ways to move, either taking 1 step at a time or 2 steps at a time, there are two ways to get to the very top, either by n-2 or n-1. As such, the minimum cost to get to stair n is the minimum of the cost of (n-2 cost + current step cost), (n-1 cost + current step cost). If at the very top, the cost of that step is 0, so we pay 0 to get to that top step.

        Uses bottom up with tabulation.
        '''
        n = len(cost)

        table = [0] * (n)
        table[0] = cost[0]
        table[1] = cost[1]

        for i in range(2, n):
            table[i] = min(table[i-1] + cost[i] , table[i-2] + cost[i])
        
        return min(table[n-1], table[n-2])

        #Even after calculating the table, the last step to get to the top floor is either by taking 1 step from n-1, or taking a 2 step from n-2. So we need to get the minimum cost of the two options. 
        