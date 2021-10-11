class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


def create_LinkedList(arr=None):
    if len(arr) == 0:
        return None
    else:
        head = ListNode(arr[0])
        temp = head
        for i in arr[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return head


def print_LinkedList(ListNode):
    while ListNode != None:
        print(ListNode.val, end="")
        print(" -> ", end="")
        ListNode = ListNode.next
    print("None")

