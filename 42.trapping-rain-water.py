#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        # two pointers
        l, r = 0, 0
        n = len(height)
        sections = []
        # finding sections that trap water
        while r < n:
            if l == r:
                r += 1
                continue
            if height[r] < height[l]:
                r += 1
            else:
                interval = height[l : r + 1]
                if len(interval) > 2:
                    sections.append(interval)
                l = r
        # for the rest part that did not parse, do it reversely to find rest sections
        if l != n:
            rest = list(reversed(height[l:]))
            l, r = 0, 0
            n = len(rest)
            while r < n:
                if l == r:
                    r += 1
                    continue
                if rest[r] < rest[l]:
                    r += 1
                else:
                    interval = rest[l : r + 1]
                    if len(interval) > 2:
                        sections.append(interval)
                    l = r
        # calculate answer
        ans = 0
        for s in sections:
            waterLine = min(s[0], s[-1])
            for val in s:
                ans += max(0, waterLine - val)
        return ans


# @lc code=end
