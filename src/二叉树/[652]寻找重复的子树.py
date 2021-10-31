# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。 
# 
#  两棵树重复是指它们具有相同的结构以及相同的结点值。 
# 
#  示例 1： 
# 
#          1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
#  
# 
#  下面是两个重复的子树： 
# 
#        2
#      /
#     4
#  
# 
#  和 
# 
#      4
#  
# 
#  因此，你需要以列表的形式返回上述重复子树的根结点。 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 324 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = {}
        repeated_roots = []

        def serialize(node):
            """序列化一个树 用来比较是否是相同树"""
            if node is None:
                return "#"
            # 拼接树
            res = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            # 统计出现次数
            if res in subtrees:
                subtrees[res] += 1
                # 出现2次时加入重复节点 其他次数不放入
                if subtrees[res] == 2:
                    repeated_roots.append(node)
            else:
                subtrees[res] = 1
            return res

        serialize(root)
        return repeated_roots


# leetcode submit region end(Prohibit modification and deletion)
