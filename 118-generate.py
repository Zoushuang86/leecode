"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
"""
执行用时：52 ms, 在所有 Python3 提交中击败了9.55%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了8.29%的用户

class Solution:
    def generate(self, numRows):
        results = []
        for i in range(1, numRows+1): # i为行数和每行
            temp = [0 for _ in range(i)]
            temp[0] = 1
            temp[-1] = 1
            for k in range(1, i-1):
                temp[k] = results[i-2][k-1] + results[i-2][k]
            results.append(temp)
        return results
"""

"""
错位相加：
  1 3 3 1 0
+ 0 1 3 3 1
------------
  1 4 6 4 1
  
执行用时：20 ms, 在所有 Python3 提交中击败了99.95%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.14%的用户
"""
class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        else:
            results = [[1]]
            while len(results) < numRows:
                newRow = [a + b for a, b in zip([0]+results[-1], results[-1]+[0])]
                results.append(newRow)
            return results


if __name__ == "__main__":
    A = 7
    s = Solution()
    print(s.generate(A))

