#给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。
#示例 1：
#输入：words = ["bella","label","roller"]
#输出：["e","l","l"]
#示例 2：
#输入：words = ["cool","lock","cook"]
#输出：["c","o"]
############################ solution 1 ############################
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        result = []
        res = [0] * 26
        for i in words[0]:
            res[ord(i) - ord("a")] += 1
        for i in range(1, len(words)):
            tmp = [0] * 26
            for j in range(len(words[i])):
                tmp[ord(words[i][j]) - ord("a")] += 1
            for k in range(26):
                res[k] = min(res[k], tmp[k])
        for i in range(26):
            while res[i] != 0:
                result.extend(chr(i + ord('a')))
                res[i] -= 1
        return result
############################ solution 2 ############################
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tmp = collections.Counter(words[0])
        res = []
        for i in range(1, len(words)):
            tmp = tmp & collections.Counter(words[i])
        for i in tmp:
            v = tmp[i]
            while v:
                res.append(i)
                v -= 1
        return res
