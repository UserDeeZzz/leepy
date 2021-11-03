# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  
#  
#  Related Topics 树 二叉搜索树 动态规划 回溯 二叉树 👍 1023 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []

        def helper(start, end):
            if end < start:
                return [None]
            res = []
            # 根节点
            for i in range(start, end + 1):
                # 所有左子树
                lefts = helper(start, i - 1)
                # 所有右子树
                rights = helper(i + 1, end)
                # 拼接
                for l in lefts:
                    for r in rights:
                        res.append(TreeNode(i, l, r))
            return res

        return helper(1, n)
# leetcode submit region end(Prohibit modification and deletion)
