#给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#示例 1：
#输入：digits = "23"
#输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#示例 2：
#输入：digits = ""
#输出：[]
#示例 3：
#输入：digits = "2"
#输出：["a","b","c"]
class Solution:
    def __init__(self):
        self.answers : List[str] = []
        self.answer : str = ''
        self.letter_map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
    def letterCombinations(self, digits: str) -> List[str]:
        self.answers.clear()
        if not digits:
            return []
        self.back_tracking(digits, 0)
        return self.answers

    def back_tracking(self, digits: str, index: int):
        if len(digits) == index:
            self.answers.append(self.answer)
            return
        letters: str = self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter
            self.back_tracking(digits, index + 1)
            self.answer = self.answer[:-1]
