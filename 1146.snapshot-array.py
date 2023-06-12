#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
class SnapshotArray:
    def __init__(self, length: int):
        self.array = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val)) #(snapId, val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        left, right = 0, len(history) - 1

        while left <= right:
            mid = (left + right) // 2
            # since inside history, the same snap_id might have multiple value
            # we have find the rightmost one (latest)
            if history[mid][0] <= snap_id: 
                left = mid + 1
            else:
                right = mid - 1

        return history[right][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

