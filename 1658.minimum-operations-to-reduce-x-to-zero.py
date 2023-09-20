#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#


# @lc code=start


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        n = len(nums)

        # use prefixSum and suffixSum, O(n)
        prefixSum = [0]
        suffixSum = [0]
        count1 = 0
        count2 = 0
        for i in range(n):
            count1 += nums[i]
            count2 += nums[n - i - 1]
            prefixSum.append(count1)
            suffixSum.append(count2)
        suffixSum = suffixSum[::-1]
        m = n + 1

        # reduce to 2 sum problem
        suffixSumVal2Idx = {}
        for i in range(m):
            suffixSumVal2Idx[suffixSum[i]] = i

        minOperation = float("inf")
        for leftIdx in range(m):
            left = prefixSum[leftIdx]
            target = x - left
            if target in suffixSumVal2Idx:
                rightIdx = suffixSumVal2Idx[target]
                if rightIdx >= leftIdx:
                    minOperation = min(minOperation, leftIdx + (m - rightIdx - 1))

        return -1 if minOperation == float("inf") else minOperation


# @lc code=end
