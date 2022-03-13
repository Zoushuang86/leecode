"""
234. 回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false


提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9


进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
from ListNode import *
"""
执行用时：620 ms, 在所有 Python3 提交中击败了64.11%的用户
内存消耗：39.8 MB, 在所有 Python3 提交中击败了82.96%的用户
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True

        # 找到中间节点mid，即前一段链表的最后一个节点
        dummy1 = ListNode(-1)
        dummy1.next = head
        mid, tail = dummy1, dummy1
        while tail.next and tail.next.next:
            mid = mid.next
            tail = tail.next.next if tail.next.next != None else tail.next

        # 后一段链表翻转
        dummy2 = ListNode(-1)
        dummy2.next = mid.next
        mid.next = None
        cur = dummy2.next.next
        dummy2.next.next = None
        while cur:
            next = cur.next
            cur.next = dummy2.next
            dummy2.next = cur
            cur = next

        # 比较两个链表
        cur1 = dummy1.next
        cur2 = dummy2.next
        while cur1:
            if cur1.val != cur2.val:
                return False
            cur2 = cur2.next
            cur1 = cur1.next
        return True

# 双指针法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next

        deleteFlag = False
        i, j = 0, len(nodes) - 1
        while i < j:
            if nodes[i] == nodes[j]:
                i += 1
                j -= 1
            else:
                if nodes[i] == nodes[j - 1]:
                    if deleteFlag:
                        return False
                    else:
                        j -= 1
                        deleteFlag = True
                elif nodes[i + 1] == nodes[j]:
                    if deleteFlag:
                        return False
                    else:
                        i += 1
                        deleteFlag = True
                else:
                    return False
        return True

if __name__ == "__main__":
    arr1 = [0,1,1,0]
    l1 = create_LinkedList(arr1)
    print_LinkedList(l1)
    res = Solution().isPalindrome(l1)
    print(res)
