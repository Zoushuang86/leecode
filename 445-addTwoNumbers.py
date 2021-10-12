"""
445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。



示例1：



输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]
示例2：

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]
示例3：

输入：l1 = [0], l2 = [0]
输出：[0]


提示：

链表的长度范围为 [1, 100]
0 <= node.val <= 9
输入数据保证链表代表的数字无前导 0


进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。
"""
from ListNode import *


class Solution:
    """
    执行用时：56 ms, 在所有 Python3 提交中击败了65.93%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了93.10%的用户
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def create_LinkedList(arr=None):
            if len(arr) == 0:
                return None
            else:
                head = ListNode(int(arr[0]))
                temp = head
                for i in arr[1:]:
                    temp.next = ListNode(int(i))
                    temp = temp.next
                return head

        num1 = 0
        temp1 = l1
        while temp1 != None:
            num1 = num1*10 + temp1.val
            temp1 = temp1.next

        num2 = 0
        temp2 = l2
        while temp2 != None:
            num2 = num2 * 10 + temp2.val
            temp2 = temp2.next
        res = list(str(num1 + num2))
        result = create_LinkedList(res)
        return result



if __name__ == "__main__":
    arr1 = [7, 2, 4, 3]
    l1 = create_LinkedList(arr1)
    arr2 = [5, 6, 4]
    l2 = create_LinkedList(arr2)
    print_LinkedList(l1)
    print_LinkedList(l2)
    new_head = Solution().addTwoNumbers(l1, l2)
    print_LinkedList(new_head)
