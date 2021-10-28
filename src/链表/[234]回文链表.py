# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,2,1]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围[1, 10⁵] 内 
#  0 <= Node.val <= 9 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 栈 递归 链表 双指针 👍 1162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        pre = head

        while fast:
            if not fast.next:
                # 奇数此时slow在中间,需要前进一步
                slow = slow.next
                break
            # 快指针前进2步
            fast = fast.next.next
            # 缓存上一个慢指针
            pre_slow = slow
            # 慢指针前进1步
            slow = slow.next
            # 上一个慢指针指向上一个反转头节点 翻转总是比慢指针慢一步
            pre_slow.next = pre
            # 更新反转头节点
            pre = pre_slow
        # 对比
        while slow:
            if pre.val != slow.val:
                return False
            slow = slow.next
            pre = pre.next
        return True




# leetcode submit region end(Prohibit modification and deletion)
