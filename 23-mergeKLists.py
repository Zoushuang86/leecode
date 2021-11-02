"""
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]


提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""
"""
执行用时：80 ms, 在所有 Python3 提交中击败了50.54%的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了93.92%的用户
"""
from ListNode import *
class Solution:
    def __mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            res = []
            index = 0
            while index < len(lists)-1:
                temp = self.__mergeTwoLists(lists[index], lists[index+1])
                res.append(temp)
                index += 2
            if index == len(lists)-1:
                res.append(lists[index])
            lists = res
        return lists[0]


if __name__ == "__main__":
    arr1 = [1,1,4,7,9]
    l1 = create_LinkedList(arr1)
    arr2 = [2,4,6,8]
    l2 = create_LinkedList(arr2)
    arr3 = []
    l3 = create_LinkedList(arr3)
    lists = [l3]
    new_head = Solution().mergeKLists(lists)
    print_LinkedList(new_head)
