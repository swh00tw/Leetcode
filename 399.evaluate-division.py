#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create a graph
        # for equations[i] = [a, b], a/b = values[i]
        # we can create an edge from a to bi and the weight is values[i]
        # and an edge from b to a, the weight is inverse number
        # then, if we want a/c, we can start from a and go to c. the answer can be obtained by multuply all weight along the path
        adjList = {}
        for i in range(len(equations)):
            src, dst = equations[i]
            weight = values[i]
            if adjList.get(src):
                adjList[src].append((dst, weight))
            else:
                adjList[src] = [(dst, weight)]
            if adjList.get(dst):
                adjList[dst].append((src, 1/weight))
            else:
                adjList[dst] = [(src, 1/weight)]
        # print(adjList)
        return [self.getAnswer(adjList, src, dst) for src, dst in queries]
        
    def getAnswer(self, adjList, src, dst):
        if src not in adjList or dst not in adjList:
            return -1.0
        if src==dst:
            return 1.0
        # bfs
        visited = {}
        for k in adjList:
            visited[k]=False
        s = [(src, 1)]
        visited[src]=True
        while s:
            curr, currVal = s.pop(0)
            # print("src: ", src, "dst: ", curr, "currVal: ",currVal)
            if curr==dst:
                return currVal
            for dstNode, weight in adjList[curr]:
                if not visited[dstNode]:
                    visited[dstNode]=True
                    s.append((dstNode, currVal*weight))
        return -1.0
        
# @lc code=end

