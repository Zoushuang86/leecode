"""
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
"""
from ListNode import *
"""
自底向上归并排序，intv = 1, 2, 4, 8...
执行用时：448 ms, 在所有 Python3 提交中击败了10.34%的用户
内存消耗：30.3 MB, 在所有 Python3 提交中击败了53.40%的用户
"""
class Solution:
    def sortList(self, head:ListNode) -> ListNode:
        # h：指向未归并链表头部
        # length：链表总长度
        # inv：归并链表的长度
        h, length, intv = head, 0, 1

        # 计算length
        while h:
            h, length = h.next, length+1

        # 虚拟头结点
        res = ListNode(-1)
        res.next = head

        while intv < length:
            # pre：指向待归并链表的前一个节点
            pre, h = res, res.next
            while h:
                # 获取两个归并链表的头节点h1,h2
                # 获取h1
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i-1

                # h1指向的链表不足inv，无需归并
                if i:
                    break

                # 获取h2和h2链表长度, 更新h
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i-1

                # 归并h1、h2
                c1, c2 = intv, intv - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 -= 1
                    pre = pre.next

                pre.next = h1 if c1 else h2

                # 归并剩余
                while c1>0 or c2>0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = h
            intv = intv*2
        return res.next


if __name__ == "__main__":
    arr1 = [4,2,1,5,6,0,1,3]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    new_head = Solution().sortList(l1)
    print_LinkedList(new_head)
