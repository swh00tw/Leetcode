#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        queue = rooms[0]
        while queue:
            idx = queue.pop(0)
            if visited[idx] is True:
                continue
            queue.extend(rooms[idx])
            visited[idx] = True
        return all(visited)


# @lc code=end
