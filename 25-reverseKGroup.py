"""
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：


输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
示例 3：

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]
示例 4：

输入：head = [1], k = 1
输出：[1]
提示：

列表中节点的数量在范围 sz 内
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
"""
"""
执行用时：36 ms, 在所有 Python3 提交中击败了93.19%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了33.54%的用户
"""
from ListNode import *
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head):
            pre = None
            curr = head
            while curr:
                next = curr.next
                curr.next = pre
                pre = curr
                curr = next
            return pre

        dummy = ListNode(-1)
        dummy.next = head
        # pre：指向待翻转区域的前一个节点
        # end：指向待翻转区域的最后一个节点
        # next：指向待翻转区域的后一个节点，即end.next
        pre, end = dummy, dummy
        while end.next:
            i = 0
            while i < k and end:
                end = end.next
                i += 1

            if end == None:
                break

            start = pre.next
            next = end.next
            end.next = None
            pre.next = reverse(start)
            start.next = next
            pre = start
            end = pre

        return dummy.next


if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    k = 4
    new_head = Solution().reverseKGroup(l1, k)
    print_LinkedList(new_head)

