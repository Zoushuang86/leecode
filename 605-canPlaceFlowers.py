"""
605. 种花问题
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），
和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
"""

"""
执行用时：48 ms, 在所有 Python3 提交中击败了97.53%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了14.65%的用户
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if flowerbed.count(1) + n > len(flowerbed) // 2 + (len(flowerbed) % 2):
            return False
        elif len(flowerbed) == 1:
            if flowerbed[0] == 0 and (n == 1 or n == 0):
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            for index in range(1, len(flowerbed)-2):
                if flowerbed[index] == 0 and flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
                    flowerbed[index] = 1
                    n -= 1
                if n == 0:
                    return True
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1
            if n <= 0:
                return True
            else:
                return False


if __name__ == "__main__":
    A = [1,0,0,0,1]
    n = 2
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], n))