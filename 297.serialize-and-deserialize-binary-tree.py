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
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "EMPTY"
        # we can store the inorder and preorder of the binary tree in the msg
        self.io = []
        self.po = []
        self.preorder(root, 0)
        self.inorder(root, 0)
        res = f"{self.po}|{self.io}"
        self.io = []
        self.po = []
        return res

    def inorder(self, node, idx):
        if node:
            self.inorder(node.left, 2 * idx + 1)
            self.io.append(node.val)
            self.io.append(idx)
            self.inorder(node.right, 2 * idx + 2)

    def preorder(self, node, idx):
        if node:
            self.po.append(node.val)
            self.po.append(idx)
            self.preorder(node.left, 2 * idx + 1)
            self.preorder(node.right, 2 * idx + 2)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "EMPTY":
            return None
        poStr, ioStr = data.split("|")
        preorderPairs = poStr[1:-1].split(",")
        inorderPairs = ioStr[1:-1].split(",")
        preorder = [
            (int(preorderPairs[i]), int(preorderPairs[i + 1]))
            for i in range(0, len(preorderPairs), 2)
        ]
        inorder = [
            (int(inorderPairs[i]), int(inorderPairs[i + 1]))
            for i in range(0, len(inorderPairs), 2)
        ]
        return self.buildTree(preorder, inorder)

    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind][0])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1 :])
            return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
