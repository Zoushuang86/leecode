"""
127. 单词接龙
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。


示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。


提示：

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
"""
"""
匹配时间过长

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        def isPath(a: str, b: str):
            a = list(a)
            b = list(b)
            flag = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if flag == False:
                        flag = True
                    else:
                        return False
            if flag == False:
                return False
            else:
                return True

        if endWord not in wordList:
            return 0

        queue = []
        queue.append([beginWord, 1])

        visited = {e: False for e in wordList}
        visited[beginWord] = True

        while len(queue) > 0:
            word = queue[0][0]
            step = queue[0][1]
            queue.pop(0)

            for e in wordList:
                if visited[e] == False:
                    if isPath(word, e):
                        if e == endWord:
                            return step + 1
                        queue.append([e, step+1])
                        visited[e] = True
        return 0
"""
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]
                    # 依次替换当前单词的某一个字母进行匹配
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dok","lot","log","cog"]
    s = Solution()
    print(s.ladderLength(beginWord, endWord, wordList))
