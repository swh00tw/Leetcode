#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS
        # maintain a stack s
        # init state: s=[(sr,sc)]
        # while s is not empty, keep pop the first item of stack and change it's color in image
        # add adjacent blocks into s if they have same original color as starting pixel
        n = len(image)
        m = len(image[0])
        s = [(sr, sc)]
        targetColor = image[sr][sc]
        if targetColor==color:
            return image
        while s:
            x, y = s.pop(0)
            image[x][y]=color
            # check the pixel above, below, left, right
            if y-1>=0 and image[x][y-1]==targetColor:
                s.append((x, y-1))
            if y+1<m and image[x][y+1]==targetColor:
                s.append((x, y+1))
            if x-1>=0 and image[x-1][y]==targetColor:
                s.append((x-1, y))
            if x+1<n and image[x+1][y]==targetColor:
                s.append((x+1, y))
        return image
# @lc code=end

