import random
from typing import TypeVar, Generic
T = TypeVar("T")


class MaxHeap:
    def __init__(self, capacity: int, arr=None):
        if arr == None:
            # index=0不存储
            self.__data = [Generic[T]] * (capacity+1)
            self.__count = 0
            self.__capacity = capacity
        else:
            self.__data = [Generic[T]] * (capacity+1)
            self.__capacity = capacity
            for i in range(self.__capacity):
                self.__data[i+1] = arr[i]
            self.__count = capacity

            for i in range(self.__count // 2, 0, -1):
                self.__shiftDown(i)

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def __shiftUp(self, k):
        while k > 1 and self.__data[k//2] < self.__data[k]:
            self.__data[k // 2], self.__data[k] = self.__data[k], self.__data[k // 2]
            k = k // 2

    def insert(self, item):
        assert self.__count + 1 <= self.__capacity
        self.__data[self.__count+1] = item
        self.__count += 1
        self.__shiftUp(self.__count)


    def __shiftDown(self, k):
        while 2*k <= self.__count:
            # 在此轮循环中，data[k]和data[j]交换位置
            j = 2*k
            if j+1 <= self.__count and self.__data[j+1] > self.__data[j]:
                j += 1
            if self.__data[k] >= self.__data[j]:
                break
            else:
                self.__data[k], self.__data[j] = self.__data[j], self.__data[k]
                k = j

    def extructMax(self):
        assert self.__count > 0
        ret = self.__data[1]
        self.__data[1], self.__data[self.__count] = self.__data[self.__count], self.__data[1]
        self.__count -= 1
        self.__shiftDown(1)
        return ret

    def getMax(self):
        return self.__data[1]

    # def __replace(self, s, rep, index):
    #     # 替换s的从index开始的部分字符串，替换长度为len(rep)
    #     prev = s[0:index]
    #     next = s[index + len(rep):len(s)]
    #     return prev + rep + next

    # def __getLevelAssign(self, limit):
    #     # 观察范围是[0, limit]的完全二叉树tree，
    #     # 然后得到tree对应的满二叉树的每层的信息
    #     # 包括 每层开始节点的所在数组索引levelStart
    #     #     每层结束节点的所在数组索引+1 levelLimit
    #     #     每层节点个数（虽然没用到）
    #     assign = []
    #     levelStart = 0
    #     levelCount = 1  # 每层节点的个数，2 的幂
    #     levelLimit = 1  # 每层节点索引的限制
    #     while (levelStart < limit):
    #         # 基本信息弄成一维数组，放到一个二维数组中，以栈的方式
    #         assign.insert(0, [levelStart, levelLimit, levelCount])
    #
    #         levelCount = levelCount << 1
    #         levelStart = levelCount - 1
    #         levelLimit += levelCount
    #     # 返回时，assign[0]是满二叉树最后一层的信息，assign[1]是满二叉树倒数第二层的信息
    #     return assign

    # def printHeap(self):
    #     heap = self.__data[1: self.__count+1]
    #     assign = self.__getLevelAssign(self.__count)  # 得到了每个数字层的信息
    #     maxLevelLen = 0
    #     maxLevelBlankNumber = 3  # 此处可调节。代表最后一层的数字之间的空格数
    #     printLi = []
    #     lastLevel = True
    #     for ass in assign:
    #         # 构建数字层
    #         levelStr = ""  # 代表数字层
    #         if lastLevel:  # 如果是最后一层（第一次循环当然是最后一层）
    #             for i in range(ass[0], ass[1]):
    #                 if i < self.__count:
    #                     levelStr += str(heap[i]) + " " * maxLevelBlankNumber
    #                 else:
    #                     levelStr += "n" + " " * maxLevelBlankNumber
    #             levelStr = levelStr[:-maxLevelBlankNumber]
    #             maxLevelLen = len(levelStr)  # 得到最大宽度
    #             lastLevel = False
    #         else:  # 如果不是最后一层的数字层
    #             # 下面最接近的数字层在printLi[1]，因为隔了一个指针层
    #             levelStr = " " * maxLevelLen
    #             takeIndex = ass[0]  # 从原始数组中取数字的开始索引
    #             # count代表在最接近的数字层遇到的孩子节点的次数
    #             # left 代表某连续两个左右孩子的左孩子的索引 （指左孩子字符串在它所在层的构建字符串中的索引）
    #             # right代表某连续两个左右孩子的右孩子的索引
    #             count = left = right = 0
    #             for index in range(len(printLi[1])):
    #                 # 当遇到连续数字字符串中第一个数字时
    #                 if printLi[1][index] != " " and (index == 0 or printLi[1][index - 1] == " "):
    #                     # 左移存储left right
    #                     left = right
    #                     right = index
    #                     count += 1
    #                     # 当遇到了偶数次孩子时，我们就可以为本层数字层加入数字字符串了
    #                     if count != 0 and count % 2 == 0:
    #                         middle = int((left + right) / 2)  # 取得一个中间位置
    #                         levelStr = self.__replace(levelStr, str(heap[takeIndex]), middle)
    #                         takeIndex += 1
    #         printLi.insert(0, levelStr)
    #
    #         # 构建完数字层，需要构建数字层之上的指针层，第一层数字层不需要，因为它是根节点
    #         if ass[0] != 0:  # 不是第一层
    #             pointerStr = " " * maxLevelLen
    #             left = True  # 先遇到的一定是左孩子
    #             # printLi[0]是下面最接近的数字层
    #             for charIndex in range(len(printLi[0])):
    #                 # 当遇到连续数字字符串中第一个数字时，添加本层的指针
    #                 if printLi[0][charIndex] != ' ' and (charIndex == 0 or printLi[0][charIndex - 1] == " "):
    #                     if left == True:  # 左孩子，那么本层添加一个/
    #                         pointerStr = self.__replace(pointerStr, "/", charIndex + 1)
    #                     else:  # 右孩子，那么本层添加一个\
    #                         pointerStr = self.__replace(pointerStr, "\\", charIndex - 1)
    #                     left = not left  # 置反
    #
    #             printLi.insert(0, pointerStr)  # 栈的方式添加
    #
    #     for i in printLi:
    #         print(i)


if __name__ == "__main__":
    n = 20
    maxheap = MaxHeap(100)
    for i in range(n):
        maxheap.insert(random.randint(0, 99))
    maxheap.printHeap()
    # while maxheap.isEmpty() == False:
    maxheap.extructMax()
    maxheap.printHeap()
