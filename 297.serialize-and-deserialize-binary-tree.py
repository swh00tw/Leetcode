#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def __init__(self):
        self.nil = "x"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # use preorder traversal
        if root is None:
            return self.nil
        res = ",".join(
            [f"{root.val}", self.serialize(root.left), self.serialize(root.right)]
        )
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.buildTree(data.split(","))

    def buildTree(self, preorder: List[str]) -> Optional[TreeNode]:
        val = preorder.pop(0)
        if val == self.nil:
            return None
        rootNode = TreeNode(int(val))
        rootNode.left = self.buildTree(preorder)
        rootNode.right = self.buildTree(preorder)
        return rootNode


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
