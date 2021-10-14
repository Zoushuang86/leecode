"""
61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。



示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]


提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
from ListNode import *
"""
执行用时：40 ms, 在所有 Python3 提交中击败了38.52%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了59.56%的用户
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head

        length = 0
        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy.next
        while cur:
            length += 1
            cur = cur.next
        k = k % length

        p, q = dummy, dummy
        for i in range(k):
            q = q.next

        while q.next:
            p, q = p.next, q.next

        q.next = dummy.next
        dummy.next = p.next
        p.next = None
        return dummy.next


if __name__ == "__main__":
    arr1 = [0,1,2]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    new_head = Solution().rotateRight(l1, 3000000)
    print_LinkedList(new_head)
