#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#


# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for mass in asteroids:
            if mass > 0:
                stack.append(mass)
            elif mass < 0:
                exploded = False
                # while loop until explode
                while stack and stack[-1] > 0:
                    if stack[-1] == abs(mass):
                        stack.pop()
                        exploded = True
                        break
                    elif stack[-1] > abs(mass):
                        exploded = True
                        break
                    else:
                        stack.pop()
                # if not explode
                if not exploded:
                    stack.append(mass)
        return stack


# @lc code=end
