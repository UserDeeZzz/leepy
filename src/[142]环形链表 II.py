# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，
# pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。 
# 
#  说明：不允许修改给定的链表。 
# 
#  进阶： 
# 
#  
#  你是否可以使用 O(1) 空间解决此题？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围在范围 [0, 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  pos 的值为 -1 或者链表中的一个有效索引 
#  
#  Related Topics 哈希表 链表 双指针 👍 1221 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 2个节点 一个走2步 一个走1步 会在1步节点没走完1圈时相遇
        if head is None:
            return
        p1 = head.next
        if p1 is None:
            return
        p2 = head.next.next
        if p2 is None:
            return

        while p1 != p2:
            if p2.next is None or p2.next.next is None:
                return
            p2 = p2.next.next
            p1 = p1.next
        # 快指针比慢指针多走n圈 n(b+c) = a + b
        # p3走a a = (n-1)b + nc  此时p1已经距离入环点b b+a = n(b+c)刚好回到入环点
        # p3 和 p1 再次相遇就是入环口
        p3 = head
        while p1 != p3:
            p1 = p1.next
            p3 = p3.next

        return p1
# leetcode submit region end(Prohibit modification and deletion)
