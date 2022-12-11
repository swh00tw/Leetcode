/*
 * @lc app=leetcode id=112 lang=typescript
 *
 * [112] Path Sum
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
// class TreeNode {
//   val: number;
//   left: TreeNode | null;
//   right: TreeNode | null;
//   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.left = left === undefined ? null : left;
//     this.right = right === undefined ? null : right;
//   }
// }

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (root === null) return false;
  const subtreeTargetSum = targetSum - root.val;
  if (root.left === null && root.right === null) {
    return subtreeTargetSum === 0;
  } else if (root.left !== null && root.right === null) {
    return hasPathSum(root.left, subtreeTargetSum);
  } else if (root.left === null && root.right !== null) {
    return hasPathSum(root.right, subtreeTargetSum);
  } else {
    return (
      hasPathSum(root.left, subtreeTargetSum) ||
      hasPathSum(root.right, subtreeTargetSum)
    );
  }
}
// @lc code=end
