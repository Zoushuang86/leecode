"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

"""
执行用时：52 ms, 在所有 Python3 提交中击败了47.02%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.41%的用户
"""
from ListNode import *

"""
执行用时：48 ms, 在所有 Python3 提交中击败了6.00%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了36.12%的用户
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_Node = ListNode(-1)
        cur = dummy_Node
        cur1 = l1 if l1 != None else None
        cur2 = l2 if l2 != None else None
        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if cur1 != None:
            cur.next = cur1

        if cur2 != None:
            cur.next = cur2

        return dummy_Node.next


if __name__ == "__main__":
    arr1 = [1,1,4,7,9]
    l1 = create_LinkedList(arr1)
    arr2 = [2,4,6,8]
    l2 = create_LinkedList(arr2)
    print_LinkedList(l1)
    print_LinkedList(l2)
    new_head = Solution().mergeTwoLists(l1, l2)
    print_LinkedList(new_head)


