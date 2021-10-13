"""
82. 删除排序链表中的重复元素 II
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表。



示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]


提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列
通过次数184,882提交次数348,260
"""
from ListNode import *
"""
执行用时：40 ms, 在所有 Python3 提交中击败了58.47%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了19.49%的用户
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


if __name__ == "__main__":
    arr1 = [1, 1, 2, 3, 3, 5]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    new_head = Solution().deleteDuplicates(l1)
    print_LinkedList(new_head)
