class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 建立二叉树是以层序遍历方式输入，节点不存在时以 'None' 表示
def creatTree(nodeList):
    if nodeList[0] == None:
        return None
    head = TreeNode(nodeList[0])
    Nodes = [head]
    j = 1
    for node in Nodes:
        if node != None:
            node.left = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.left)
            j += 1
            if j == len(nodeList):
                return head
            node.right = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
            j += 1
            Nodes.append(node.right)
            if j == len(nodeList):
                return head


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)
