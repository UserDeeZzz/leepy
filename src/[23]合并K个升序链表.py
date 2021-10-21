# 给你一个链表数组，每个链表都已经按升序排列。
#
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
#  示例 1：
#
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
#  示例 2：
#
#  输入：lists = []
# 输出：[]
#
#
#  示例 3：
#
#  输入：lists = [[]]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  k == lists.length
#  0 <= k <= 10^4
#  0 <= lists[i].length <= 500
#  -10^4 <= lists[i][j] <= 10^4
#  lists[i] 按 升序 排列
#  lists[i].length 的总和不超过 10^4
#
#  Related Topics 链表 分治 堆（优先队列） 归并排序 👍 1554 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class HeapQ:

    def __init__(self):
        self.rq = []
        self.size = 0

    def push(self, node: ListNode):
        """
        添加新元素到最后
        从最后位置开始上浮
        """
        self.rq.append(node)
        self.size += 1
        self.swim(self.size - 1)

    def swim(self, i):
        """
        上浮
        """
        if i != 0:
            parent = (i - 1) // 2
            if parent >= 0 and self.rq[i].val < self.rq[parent].val:
                self.exchange(parent, i)
                self.swim(parent)

    def exchange(self, i, j):
        self.rq[i], self.rq[j] = self.rq[j], self.rq[i]

    def sink(self, i):
        """
        下沉
        """
        left = 2 * i + 1
        right = 2 * i + 2
        if left <= self.size - 1 and self.rq[left].val < self.rq[i].val:
            self.exchange(left, i)
            self.sink(left)
        if right <= self.size - 1 and self.rq[right].val < self.rq[i].val:
            self.exchange(right, i)
            self.sink(right)

    def pop(self):
        """
        元素0和最后一个互换
        删除元素0
        最后一个元素开始下沉
        :return:
        """
        if self.size != 0:
            self.exchange(0, -1)
            node = self.rq.pop(-1)
            self.size -= 1
            self.sink(0)
            return node


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        pointer = dummy
        hq = HeapQ()
        for l in lists:
            if l:
                hq.push(l)
        while hq.size:
            node = hq.pop()
            pointer.next = node
            pointer = node
            if node.next:
                hq.push(node.next)
        return dummy.next
