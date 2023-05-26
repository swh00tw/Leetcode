#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack)>=2 and stack[-1]<0 and stack[-2]>0:
                s1 = stack.pop()
                s2 = stack.pop()
                if abs(s1)>abs(s2):
                    stack.append(s1)
                elif abs(s2)>abs(s1):
                    stack.append(s2)
        return stack
        
# @lc code=end

