"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。

例如，下面的二进制手表读取 "3:25" 。


（图源：WikiMedia - Binary clock samui moon.jpg ，许可协议：Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) ）

给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。

小时不会以零开头：

例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
分钟必须由两位数组成，可能会以零开头：

例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
 

示例 1：

输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
示例 2：

输入：turnedOn = 9
输出：[]
 

提示：

0 <= turnedOn <= 10
"""
class Solution:
    res = []

    def __convert(self, pre):
        hour = (0b1111000000 & pre) >> 6
        minute = 0b0000111111 & pre
        if hour > 11:
            return None
        if minute > 59:
            return None
        string = str(hour)+":"
        if minute < 10:
            string += "0"
        string += str(minute)
        return string

    def __dfs(self, turnedOn, index, pre):
        if turnedOn == 0:
            string = self.__convert(pre)
            if string != None:
                self.res.append(string)
            return

        if 10 - index < turnedOn:
            return

        self.__dfs(turnedOn - 1, index + 1, pre + pow(2, index))
        self.__dfs(turnedOn, index + 1, pre)


    def readBinaryWatch(self, turnedOn: int) -> list:
        self.res.clear()
        if turnedOn > 8:
            return []
        self.__dfs(turnedOn, 0, 0)
        return self.res


if __name__ == "__main__":
    turnedOn = 2
    s = Solution()
    k = s.readBinaryWatch(turnedOn)
    print(k)
