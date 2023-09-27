#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#


# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}  # map letter to last occur idx
        stack = []  # stack current letters
        seen = set()  # all letters in the current stack
        for i, c in enumerate(s):
            last_occur[c] = i

        # property we maintain:
        # the current stack must always be the smallest in lexicographical order
        for i, c in enumerate(s):
            # if it's in current stack, skip it since the stack is already optimized based on the property
            # if it's not in the stack, find the insert position by keep popping the top of the stack and insert it
            # special case: if the letter is in last_occur_idx, should not pop it
            if c not in seen:
                while stack and stack[-1] > c and i < last_occur[stack[-1]]:
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(c)
                seen.add(c)
        return "".join(stack)


# @lc code=end
