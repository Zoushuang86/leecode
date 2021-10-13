"""
147. 对链表进行插入排序
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。



插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。


示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""
from ListNode import *
"""
执行用时：136 ms, 在所有 Python3 提交中击败了91.08%的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了61.77%的用户
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        last = head
        cur = head.next
        while cur:
            if last.val <= cur.val:
                last = last.next
            else:
                pre = dummy
                while pre.next.val <= cur.val:
                    pre = pre.next
                last.next = cur.next
                cur.next = pre.next
                pre.next =cur
            cur = last.next
        return dummy.next


if __name__ == "__main__":
    arr1 = [4,2,1,5,6,0,1,3]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    new_head = Solution().insertionSortList(l1)
    print_LinkedList(new_head)
