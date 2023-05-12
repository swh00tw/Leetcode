#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberFreq = {}
        for n in nums:
            if numberFreq.get(n):
                numberFreq[n] += 1
            else:
                numberFreq[n] = 1
        kvs = []
        for key in numberFreq:
            kvs.append([key, numberFreq[key]])
        sorted_kvs = list(sorted(kvs, key= lambda x:-x[1]))
        ans = [sorted_kvs[i][0] for i in range(k)]
        return ans
# @lc code=end

