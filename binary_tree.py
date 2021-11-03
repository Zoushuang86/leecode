from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BT:
    def __init__(self, l=None):
        if l[0]:
            self.root = TreeNode(l[0])
            nodes = [self.root]
            id = 1
            while nodes and id < len(l):
                node = nodes[0]  # 依次为每个节点分配子节点
                node.left = TreeNode(l[id]) if l[id] else None
                if node.left:
                    nodes.append(node.left)
                node.right = TreeNode(l[id + 1]) if id < len(l) - 1 and l[id + 1] else None
                if node.right:
                    nodes.append(node.right)
                id += 2  # 每次取出两个节点
                nodes.pop(0)
        else:
            self.root = None
