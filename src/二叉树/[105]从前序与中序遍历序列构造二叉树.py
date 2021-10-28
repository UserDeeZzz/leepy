# 给定一棵树的前序遍历 preorder 与中序遍历 inorder。请构造二叉树并返回其根节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder 和 inorder 均无重复元素 
#  inorder 均出现在 preorder 
#  preorder 保证为二叉树的前序遍历序列 
#  inorder 保证为二叉树的中序遍历序列 
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 1274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # 根节点位置先序遍历第一个
        inorder_idx = inorder.index(preorder[0])
        # 左子树
        root.left = self.buildTree(preorder[1:inorder_idx + 1], inorder[:inorder_idx])
        # 右子树
        root.right = self.buildTree(preorder[inorder_idx + 1:], inorder[inorder_idx + 1:])
        return root
# leetcode submit region end(Prohibit modification and deletion)
