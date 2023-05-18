#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # find all node woth indegree == 0 and return
        # since node with 0 indegree (nobody point to them) cannot be reached
        # they must in the subset
        # for other node with indegree > 0
        # they must can be reached from the adjacent node x since x must can be reached (if x can't be reached, x will have indegree == 0 and we will start on x)
        # that is to say, for nodes with indegree>0, they must can be reached anyway
        indegree = [0]*n
        for src, dst in edges:
            indegree[dst]+=1
        ans = []
        for i in range(n):
            if indegree[i]==0:
                ans.append(i)
        return ans
            

                    

        
# @lc code=end

