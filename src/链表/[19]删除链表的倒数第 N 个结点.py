# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 
# 
#  进阶：你能尝试使用一趟扫描实现吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1], n = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
#  Related Topics 链表 双指针 👍 1615 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy,1,2,3,4 倒数第2个 应该走到2这个节点 差2步 也就是head先走n步
        dummy = ListNode(-1)
        dummy.next = head
        pointer = dummy  # 指向被删除节点的前一个 也就是倒数n + 1节点

        i = 0
        while head:
            head = head.next
            if i < n:
                i += 1
            else:
                pointer = pointer.next

        pointer.next = pointer.next.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
