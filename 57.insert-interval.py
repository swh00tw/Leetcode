#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
# ref: https://leetcode.com/problems/insert-interval/solutions/4213475/detailed-solution-in-python3-go-ts-with-o-n-time-and-space-complexity
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Initialize an output container
        output = []

        # Iterate through all intervals
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])

            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        # Add the new interval to the output if not added already
        # ! No need for conditions as we would not reach this point otherwise
        output.append(newInterval)
        # Return the final output
        return output


# @lc code=end
