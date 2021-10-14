#给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#注意：
#对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
#如果 s 中存在这样的子串，我们保证它是唯一的答案。
#示例 1：
#输入：s = "ADOBECODEBANC", t = "ABC"
#输出："BANC"
#示例 2：
#输入：s = "a", t = "a"
#输出："a"
#示例 3:
#输入: s = "a", t = "aa"
#输出: ""
#解释: t 中两个字符 'a' 均应包含在 s 的子串中，
#因此没有符合条件的子字符串，返回空字符串。
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m: 
            return ""
        
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1  
        need_cnt = m
        res = [0, n]

        left = 0 
        for right, c in enumerate(s):
            if need[c] > 0:
                need_cnt -= 1
            need[c] -= 1
            if need_cnt == 0:
                while True:
                    if need[s[left]] == 0:
                        break
                    need[s[left]] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = [left, right]
        if res != [0, n]:
            return s[res[0]: res[1] + 1]
        else:
            return ""
