"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]


提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""
class Solution:
    letterMap = {'2': "abc", "3": "def", "4": "ghi",
                 "5": "jkl", "6": "mno", "7": "pqrs",
                 "8": "tuv", "9": "wxyz"}

    res = []
    def letterCombinations(self, digits: str) -> list:
        self.res.clear()
        if len(digits) == 0:
            return self.res
        self.__findCombination(digits, 0, "")
        return self.res


    def __findCombination(self, digits: str, index: int, s: str):
        """
        :param s: 保存了此时从digits[0,index-1]翻译得到的一个字母字符串
        """
        print("{} : {}".format(index, s))
        if index == len(digits):
            self.res.append(s)
            print("get {}, return".format(s))
            return
        char = digits[index]
        letters = self.letterMap[char]
        for e in letters:
            print("digits[{}] = {} use {}".format(index, char, e))
            self.__findCombination(digits, index+1, s + e)
        return


if __name__ == "__main__":
    A = "234"
    s = Solution()
    print(s.letterCombinations(A))
