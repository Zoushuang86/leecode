"""
剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。



示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。


提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    方法一：拼接+拆分
    考虑构建 原节点 1 -> 新节点 1 -> 原节点 2 -> 新节点 2 -> …… 的拼接链表，
    如此便可在访问原节点的 random 指向节点的同时找到新对应新节点的 random 指向节点。
    """
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head

        # 创建新节点并插入原链表
        cur = head
        while cur:
            temp = Node(cur.val, cur.next)
            cur.next = temp
            cur = temp.next

        # 构建新节点的random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 拆分两个链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = cur.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res

    """
    方法二：哈希表
    """
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head

        # 构建新旧节点映射
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        # 构建新节点的random和next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next

        return dic[head]
