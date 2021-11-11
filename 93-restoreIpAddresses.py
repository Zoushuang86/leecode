"""
93. 复原 IP 地址
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按 任何 顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。



示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


提示：

0 <= s.length <= 3000
s 仅由数字组成
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        if len(s) < 4 or len(s) > 12:
            return []

        SEG_COUNT = 4
        res = []
        segments = [0] * SEG_COUNT

        def dfs(segId: int, segStart: int):
            # 如果找到了4段IP地址并且遍历完了字符串，那么就是一种答案
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipArr = ".".join(str(seg) for seg in segments)
                    res.append(ipArr)
                return

            # 如果还没找到4段IP地址就遍历完了字符串，那么提前回溯
            if segStart == len(s):
                return

            # 如果当前数字为0，那么这一段IP地址只能为0
            if s[segStart] == '0':
                segments[segId] = 0
                dfs(segId+1, segStart+1)

            # 一般情况进行枚举
            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr*10 + int(s[segEnd])
                if 0 < addr <= 255:
                    segments[segId] = addr
                    dfs(segId+1, segEnd+1)
                else:
                    return

        dfs(0, 0)
        return res


if __name__ == "__main__":
    A = "25525511135"
    s = Solution()
    print(s.restoreIpAddresses(A))
