"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]


提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100


进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）
"""
from ListNode import *
"""
执行用时：32 ms, 在所有 Python3 提交中击败了65.83%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.69%的用户
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        p = dummy
        while p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next
            next = node2.next

            node2.next = node1
            node1.next = next
            p.next = node2

            p = node1

        return dummy.next


if __name__ == "__main__":
    arr1 = [1,2,4,7]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    new_head = Solution().swapPairs(l1)
    print_LinkedList(new_head)

