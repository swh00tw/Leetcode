#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        q = [0]
        visited[0] = True
        while q:
            roomIdx = q.pop(0)
            keys = rooms[roomIdx]
            for key in keys:
                if visited[key]==False:
                    visited[key]=True
                    q.append(key)
        return all(visited)
        
# @lc code=end

