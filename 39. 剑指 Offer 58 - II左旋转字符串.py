#字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
#示例 1：
#输入: s = "abcdefg", k = 2
#输出: "cdefgab"
#示例 2：
#输入: s = "lrloseumgh", k = 6
#输出: "umghlrlose"
######################## solution 1 ########################
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
######################## solution 2 ########################
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        s[0:n] = list(reversed(s[0:n]))
        s[n:] = list(reversed(s[n:]))
        s.reverse()
        
        return "".join(s)
######################## solution 3 ########################
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        new_s = ''
        for i in range(len(s)):
            j = (i + n) % len(s)
            new_s = new_s + s[j]
        return new_s
######################## solution 4 ########################
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        def reverse_sub(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        
        res = list(s)
        end = len(res) - 1
        reverse_sub(res, 0, n - 1)
        reverse_sub(res, n, end)
        reverse_sub(res, 0, end)
        return ''.join(res)
