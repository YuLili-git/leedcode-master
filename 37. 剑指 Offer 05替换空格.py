#请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#示例 1：
#输入：s = "We are happy."
#输出："We%20are%20happy."
########################## solution 1 ##########################
class Solution:
    def replaceSpace(self, s: str) -> str:

        res = []
        for i in s:
            if i == ' ':
                res.append("%20")
            else:
                res.append(i)
        return ''.join(res)
########################## solution 2 ##########################
class Solution:
    def replaceSpace(self, s: str) -> str:
        count = s.count(' ')
        res = list(s)
        res.extend([' '] * count * 2)
        left = len(s) - 1
        right = len(res) - 1
        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right - 2: right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)
