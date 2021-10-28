# 根据一棵树的中序遍历与后序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 607 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        # 根节点
        root = TreeNode(postorder[-1])
        inorder_idx = inorder.index(postorder[-1])
        # 左子树
        root.left = self.buildTree(inorder[:inorder_idx], postorder[:inorder_idx])
        # 右子树
        root.right = self.buildTree(inorder[inorder_idx + 1:], postorder[inorder_idx:-1])
        return root
# leetcode submit region end(Prohibit modification and deletion)
