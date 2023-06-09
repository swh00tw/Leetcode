#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary search (rightmost)
        n = len(letters)
        l, r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            if target<letters[mid]:
                r = mid-1
            else:
                l = mid+1
        return letters[l] if 0<=l<n else letters[0]
        
# @lc code=end

