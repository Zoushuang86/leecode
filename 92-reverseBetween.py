"""
92. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]


提示：

链表中节点数目为 n
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""
from ListNode import *


"""
方法一：压入栈重新赋值
执行用时：32 ms, 在所有 Python3 提交中击败了68.39%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了55.38%的用户

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        stuck = []
        index = 0
        temp = head
        while index <= right and temp!=None:
            index += 1
            if left <= index <= right:
                if index == left:
                    left_node = temp
                stuck.append(temp.val)
            temp = temp.next
        for i in stuck[::-1]:
            left_node.val = i
            left_node = left_node.next
        return head
"""
"""
方法二：穿针引线+头插法
执行用时：24 ms, 在所有 Python3 提交中击败了97.65%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了70.95%的用户
"""
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 防止头节点也会被反转
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        # 将pre定位到需要反转区间节点的前一个节点
        for _ in range(left-1):
            pre = pre.next
        cur = pre.next
        for _ in range(right-left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next


if __name__ == "__main__":
    arr = [0, 1, 2, 3 ,4, 5, 6]
    head = create_LinkedList(arr)
    print_LinkedList(head)
    new_head = Solution().reverseBetween(head, 4, 6)
    print_LinkedList(new_head)
