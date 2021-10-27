#给你一个字符串 s ，逐个翻转字符串中的所有 单词 。
#单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
#请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。
#说明：
#输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
#翻转后单词间应当仅用一个空格分隔。
#翻转后的字符串中不应包含额外的空格。
#示例 1：
#输入：s = "the sky is blue"
#输出："blue is sky the"
#示例 2：
#输入：s = "  hello world  "
#输出："world hello"
#解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。
#示例 3：
#输入：s = "a good   example"
#输出："example good a"
#解释：如果两个单词间有多余的空格，将翻转后单词间的空格减少到只含一个。
#示例 4：
#输入：s = "  Bob    Loves  Alice   "
#输出："Alice Loves Bob"
#示例 5：
#输入：s = "Alice does not even like bob"
#输出："bob like even not does Alice"
class Solution:
    def trim_spaces(self,s):
        n = len(s)
        left = 0
        right = n - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        tmp = []
        while left <= right:
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':
                tmp.append(s[left])
            left += 1
        return tmp

    def reverse_string(self,nums,left,right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None

    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums,start,end-1)
            start = end + 1
            end += 1
        return None

    def reverseWords(self, s: str) -> str:
        res = self.trim_spaces(s)
        self.reverse_string( res,  0, len(res) - 1)
        self.reverse_each_word(res)
        return ''.join(res)
