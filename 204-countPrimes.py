"""
204. 计数质数
统计所有小于非负整数 n 的质数的数量。

质数（Prime number），又称素数，指在大于 1 的自然数中，除了 1 和该数自身外，
无法被其他自然数整除的数。 ———维基百科

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0


提示：

0 <= n <= 5 * 106
"""

"""
# 暴力法超时
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        else:
            import math
            count = 0
            for i in range(2, n):
                flagPrime = True
                for j in range(2, int(math.sqrt(i))+1):
                    if i % j == 0:
                        flagPrime = False
                        break
                if flagPrime:
                    count += 1
            return count
"""

"""
厄拉多塞筛法，简称埃氏筛
这是一个古老的筛素数的方法。方法如下：
1. 初始化长度 O(n)的标记数组，表示这个数组是否为质数。数组初始化所有的数都是质数.
2. 从 2 开始将当前数字的倍数全都标记为合数。标记到sqrt(n)时停止即可。
注意:每次找当前素数 x 的倍数时，是从 x^2开始的。
因为如果 x > 2，那么 2*x 肯定被素数 2 给过滤了，最小未被过滤的肯定是 x^2 。

时间复杂度：O(nloglog(n))。松的上界 O(nlogn)。
空间复杂度：O(n)，用来标记是否为质数。

执行用时：400 ms, 在所有 Python3 提交中击败了65.68%的用户
内存消耗：37.4 MB, 在所有 Python3 提交中击败了7.10%
的用户
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        listPrimes = [True for i in range(n)]
        i = 2
        while i * i < n:
            if listPrimes[i]:
                for j in range(i*i, n, i):
                    listPrimes[j] = False
            i += 1
        return listPrimes[2:].count(True)

"""
线性筛
埃氏筛其实还是存在冗余的标记操作，比如对于 4545 这个数，它会同时被 3,53,5 两个数标记为合数。
因此我们优化的目标是让每个合数只被标记一次。
相较于埃氏筛，我们多维护一个 primes 数组表示当前得到的质数集合。我们从小到大遍历，如果当前的数 x 是质数，就将其加入 primes 数组。

另一点与埃氏筛不同的是，「标记过程」不再仅当 x 为质数时才进行，而是对每个整数 x 都进行。对于整数 x，我们不再标记其所有的倍数 x*x,
x * (x+1),…，而是只标记质数集合中的数与 x 相乘的数，即 x*primes_0,x*primes_1,…，且在发现 x mod primes_i=0 的时候结束当前标记。
"""

if __name__ == "__main__":
    A = 10
    s = Solution()
    print(s.countPrimes(A))

