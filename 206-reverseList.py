"""
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
方法一：利用外部空间
执行用时：48 ms, 在所有 Python3 提交中击败了34.56%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了40.00%的用户

时间复杂度：O(2*n) + O(n) = O(n)
空间复杂度：O(n) + O(1) = O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        val = []
        node = head
        while node:
            val.append(node.val)
            node = node.next
        node = head
        val = reversed(val)
        for i in val:
            node.val = i
            node = node.next
        return head
"""
"""
方法二：迭代
我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
第二个指针 cur 指向 head，然后不断遍历 cur。
每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。

执行用时：40 ms, 在所有 Python3 提交中击败了80.49%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了38.67%的用户

class Solution(object):
    def reverseList(self, head):
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre
"""

"""
方法三：3指针pre、cur、next
执行用时：36 ms, 在所有 Python3 提交中击败了61.08%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了47.38%的用户
"""
class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


def print_ListNode(ListNode):
    while ListNode != None:
        print(ListNode.val, end="")
        print("->", end="")
        ListNode = ListNode.next
    print("None")


if __name__ == "__main__":
    head = ListNode(0)
    next = head
    for i in range(1, 6):
        next.next = ListNode(i)
        next = next.next
    new_head = Solution().reverseList(head)
    print_ListNode(new_head)
