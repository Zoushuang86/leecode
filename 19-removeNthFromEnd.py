"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？



示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]


提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
from ListNode import *
"""
双指针
执行用时：32 ms, 在所有 Python3 提交中击败了71.34%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了78.13%的用户
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        p, q = dummy, dummy
        for i in range(n+1):
            q = q.next

        while q:
            p = p.next
            q = q.next

        p.next = p.next.next

        return dummy.next


if __name__ == "__main__":
    arr1 = [4]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    new_head = Solution().removeNthFromEnd(l1, 1)
    print_LinkedList(new_head)
