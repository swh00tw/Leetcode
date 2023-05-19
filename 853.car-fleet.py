#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # ref: https://leetcode.com/problems/car-fleet/solutions/139850/c-java-python-straight-forward/
        # sort car by its position (desc)
        # count the time to reach goal
        # iterate through each car
        # keep track of the maximum time needed, we've seen so far (slowest)
        # if we find the time to reach goal is lower than previous car, it means its gonna catch up
        # merge than into a fleet (do nothing)
        # if we find a car has remaining time larger than maximum time needed, there's a new fleet (it become the slowest)
        # increment the fleet count
        sortedPsp = sorted(zip(position, speed), key=lambda x: -x[0])
        time = [float(target - p) / s for p, s in sortedPsp]

        slowest = time[0]
        fleet = 1
        if len(time)>1:
            for i in range(1,len(time)):
                if time[i] > slowest:
                    slowest = time[i]
                    fleet += 1
        return fleet
        

# @lc code=end

