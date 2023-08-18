#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#


# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # greedy
        degree = {}
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            degree[i] = 0
        for start, end in roads:
            degree[start] += 1
            degree[end] += 1
            graph[start][end] = 1
            graph[end][start] = 1

        ans = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = max(ans, degree[i] + degree[j] + (-1 if graph[i][j] == 1 else 0))
        return ans


# @lc code=end
