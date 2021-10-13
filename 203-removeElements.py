"""
203. 移除链表元素
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。


示例 1：


输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：

输入：head = [], val = 1
输出：[]
示例 3：

输入：head = [7,7,7,7], val = 7
输出：[]


提示：

列表中的节点数目在范围 [0, 104] 内
1 <= Node.val <= 50
0 <= val <= 50
"""
from ListNode import *
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None

        while head != None and head.val == val:
            head = head.next

        if head == None:
            return None

        cur = head
        while cur.next != None:
            if cur.next.val == val:
                # 删除cur.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
"""
"""
执行用时：52 ms, 在所有 Python3 提交中击败了90.67%的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了59.02%的用户
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_Head = ListNode(-1)
        dummy_Head.next = head

        cur = dummy_Head
        while cur.next != None:
            if cur.next.val == val:
                # 删除cur.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_Head.next


if __name__ == "__main__":
    arr1 = [1, 1, 1]
    l1 = create_LinkedList(arr1)
    val = 1
    print_LinkedList(l1)
    new_head = Solution().removeElements(l1, val)
    print_LinkedList(new_head)
