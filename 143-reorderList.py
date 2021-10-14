"""
143. 重排链表
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

 L0 → L1 → … → Ln-1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例 1:



输入: head = [1,2,3,4]
输出: [1,4,2,3]
示例 2:



输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]


提示：

链表的长度范围为 [1, 5 * 104]
1 <= node.val <= 1000
"""
from ListNode import *
"""
执行用时：60 ms, 在所有 Python3 提交中击败了94.28%的用户
内存消耗：23.1 MB, 在所有 Python3 提交中击败了75.63%的用户
"""
class Solution:
    def reorderList(self, head: ListNode):
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return head

        # 找到中间节点mid，即前一段链表的最后一个节点
        dummy1 = ListNode(-1)
        dummy1.next = head
        mid, tail = dummy1, dummy1
        while tail.next and tail.next.next:
            mid = mid.next
            tail = tail.next.next if tail.next.next != None else tail.next

        # 后一段链表翻转
        dummy2 = ListNode(-1)
        dummy2.next = mid.next
        mid.next = None
        cur = dummy2.next.next
        dummy2.next.next = None
        while cur:
            next = cur.next
            cur.next = dummy2.next
            dummy2.next = cur
            cur = next

        # 合并两个链表
        cur1 = dummy1.next
        cur2 = dummy2.next
        # 记录链表尾部
        pre = dummy2
        while cur1:
            next2 = cur2.next
            next1 = cur1.next
            cur2.next = next1
            cur1.next = cur2
            cur1 = next1
            pre = cur2
            cur2 = next2

        # 处理后一个链表有剩余情况
        if cur2:
            pre.next = cur2
        return head


if __name__ == "__main__":
    arr1 = [1,2,3,4]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    h1 = Solution().reorderList(l1)
    print_LinkedList(h1)
