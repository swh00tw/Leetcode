#
# @lc app=leetcode id=2218 lang=python3
#
# [2218] Maximum Value of K Coins From Piles
#

# @lc code=start

# ref: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/solutions/3418129/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # dp[i][j] is the answer for i piles and j chances
        # example, if , k = 4, dp[3][3] might derive from dp[2][3] or (pile3[1:n] + dp[3][4-n])
        # fill the table step by step to get the answer
        dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]
        for i in range(1, len(piles) + 1):
            for j in range(1, k + 1):
                cur = 0
                for x in range(min(len(piles[i - 1]), j)):
                    cur += piles[i - 1][x]
                    dp[i][j] = max(dp[i][j], cur + dp[i - 1][j - x - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
        return dp[len(piles)][k]

# My answer (83/122 WA)
# class Merchandise:
#     def __init__(self, cost: int, degree: int, pileIdx: int):
#         self.cost = cost
#         self.degree = degree # must >=1
#         self.cpValue = cost/degree
#         self.pileIdx = pileIdx
#         self.isAvaliable = True
#     def update(self, newCost, newDegree):
#         self.cost = newCost
#         self.degree = newDegree
#         self.cpValue = newCost/newDegree
#     def markAsNA(self):
#         self.isAvaliable = False
#     def __repr__(self):
#         return f"pile {self.pileIdx}: {self.cpValue}({self.degree})"
    
# def updateMerchs(merchs, restQuota):
#     res = sorted(list(filter(lambda x:x.isAvaliable==True and x.degree<=restQuota, merchs)),key=lambda x:-x.cpValue)
#     print(res)
#     return res

# class Solution:
#     def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
#         # reduce to knapsack problem
#         merchs = []
#         for pileIdx, pile in enumerate(piles):
#             sum = 0
#             for i, coin in enumerate(pile):
#                 sum += coin
#                 merchs.append(Merchandise(sum, i+1, pileIdx))
#         # apply greedy algorithm
#         quota = k
#         merchs=updateMerchs(merchs, quota)
#         ans = 0
#         while quota>0:
#             if len(merchs)==0:
#                 break
#             # find the one with largest cpValue and pop
#             popIdx = 0
#             maxCpValue = -1
#             for i, merch in enumerate(merchs):
#                 if merch.isAvaliable and quota >= merch.degree and merch.cpValue > maxCpValue:
#                     popIdx = i
#                     maxCpValue = merch.cpValue

#             m = merchs.pop(popIdx)
#             # update merchs at the same pile
#             for i, merch in enumerate(merchs):
#                 if merch.pileIdx == m.pileIdx:
#                     newDegree = merch.degree-m.degree
#                     if newDegree<=0:
#                         # mark as not avaliable
#                         merch.markAsNA()
#                     else:
#                         merch.update(merch.cost-m.cost,newDegree)
            
#             quota -= m.degree
#             ans += m.cost
#             print(f"{quota} LEFT, total: {ans}")
#             merchs=updateMerchs(merchs, quota)
        
#         return ans

# @lc code=end

