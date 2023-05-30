#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.buckets[index]

    def _hash(self, key: int) -> int:
        return key % self.size

    # ---- My first sol ----
    # def __init__(self):
    #     self.keys = []

    # def add(self, key: int) -> None:
    #     found, insertPosition = self.binarySearch(key)
    #     if not found:
    #         self.keys.insert(insertPosition, key)

    # def remove(self, key: int) -> None:
    #     found, insertPosition = self.binarySearch(key)
    #     if found:
    #         self.keys.pop(insertPosition)

    # def contains(self, key: int) -> bool:
    #     found, insertPosition = self.binarySearch(key)
    #     return found

    # def binarySearch(self, key):
    #     l = 0
    #     r = len(self.keys)-1
    #     while l<=r:
    #         mid = (l+r)//2
    #         if key<self.keys[mid]:
    #             r = mid -1
    #         elif key>self.keys[mid]:
    #             l = mid +1
    #         else:
    #             return [True, mid]
    #     # return (found, insertPoint)
    #     return [False, l]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

