#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict


class Data:
    def __init__(self, val, ts):
        self.val = val
        self.ts = ts


class TimeMap:
    def __init__(self):
        # value is an array of Data
        self.db = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key].append(Data(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.db[key]
        if len(arr) == 0:
            return ""
        if timestamp < arr[0].ts:
            return ""
        if timestamp > arr[-1].ts:
            return arr[-1].val
        # use binary search
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            midData = arr[mid]
            if midData.ts == timestamp:
                return midData.val
            if midData.ts > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return arr[r].val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
