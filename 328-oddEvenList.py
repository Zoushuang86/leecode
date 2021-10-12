from ListNode import *
"""
328. 奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
"""
"""
执行用时：40 ms, 在所有 Python3 提交中击败了61.21%的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了75.53%的用户

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head
        cur1, cur2, cur = head, head.next, head.next.next
        while cur2 != None and cur2.next != None:
            cur = cur2.next
            cur2.next = cur.next
            cur.next = cur1.next
            cur1.next = cur
            cur1 = cur1.next
            cur2 = cur2.next

        return head
"""
"""
执行用时：36 ms, 在所有 Python3 提交中击败了82.74%的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了52.42%的用户
"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd, even = ListNode(), ListNode()
        cur1, cur2, cur = odd, even, head
        index = 1
        while cur:
            if index % 2 == 1:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
            index += 1
        cur1.next = even.next
        cur2.next = None
        return odd.next


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    head = create_LinkedList(arr)
    print_LinkedList(head)
    new_head = Solution().oddEvenList(head)
    print_LinkedList(new_head)