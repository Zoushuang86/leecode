from ListNode import *
"""
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

 

示例 1：


输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]
 

提示：

链表中节点的数目在范围 [0, 200] 内
-100 <= Node.val <= 100
-200 <= x <= 200
"""
"""
执行用时：32 ms, 在所有 Python3 提交中击败了76.98%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了11.68%的用户
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1, dummy2 = ListNode(), ListNode()
        cur1, cur2, cur = dummy1, dummy2, head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur1.next = dummy2.next
        cur2.next = None
        return dummy1.next


if __name__ == "__main__":
    arr = [1,10,3,7,9,5]
    head = create_LinkedList(arr)
    print_LinkedList(head)
    new_head = Solution().partition(head, 5)
    print_LinkedList(new_head)
