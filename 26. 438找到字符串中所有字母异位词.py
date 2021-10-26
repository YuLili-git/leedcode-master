#给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#示例 1:
#输入: s = "cbaebabacd", p = "abc"
#输出: [0,6]
#解释:
#起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
#起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 示例 2:
#输入: s = "abab", p = "ab"
#输出: [0,1,2]
#解释:
#起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
#起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
#起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        if n < m:
            return []
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        for i in range(m):
            p_cnt[ord(p[i]) - ord("a")] += 1

        left = 0
        for right in range(n):
            cur_right = ord(s[right]) - ord('a')
            s_cnt[cur_right] += 1
            while s_cnt[cur_right] > p_cnt[cur_right]:
                cur_left = ord(s[left]) - ord('a')
                s_cnt[cur_left] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)
        return res

