"""
451. 根据字符出现频率排序
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
"""
import random

"""
执行用时：64 ms, 在所有 Python3 提交中击败了32.96%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了31.35%的用户
"""
class Solution:
    def __partition(self, arr, left, right, key):

        random_index = random.randint(left, right)
        arr[left], arr[random_index] = arr[random_index], arr[left]
        key[left], key[random_index] = key[random_index], key[left]

        v = arr[left]

        j = left
        for i in range(left + 1, right + 1):
            if arr[i] < v:
                arr[j + 1], arr[i] = arr[i], arr[j + 1]
                key[j + 1], key[i] = key[i], key[j + 1]
                j += 1
        arr[left], arr[j] = arr[j], arr[left]
        key[left], key[j] = key[j], key[left]
        return j

    # 对arr[left:right+1]进行快速排序
    def __quick_sort(self, arr, left, right, key):
        if left >= right:
            return

        p = self.__partition(arr, left, right, key)
        self.__quick_sort(arr, left, p - 1, key)
        self.__quick_sort(arr, p + 1, right, key)

    def frequencySort(self, s: str) -> str:
        count = []
        key = []
        for e in s:
            if e not in key:
                count.append(1)
                key.append(e)
            else:
                count[key.index(e)] += 1
        self.__quick_sort(count, 0, len(count)-1, key)

        res = ""
        for i in range(len(count)-1, -1, -1):
            for j in range(count[i]):
                res += key[i]
        return res


if __name__ == "__main__":
    A = "Aabb"
    s = Solution()
    print(s.frequencySort(A))
