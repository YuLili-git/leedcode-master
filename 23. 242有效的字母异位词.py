#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#示例 1:
#输入: s = "anagram", t = "nagaram"
#输出: true
#示例 2:
#输入: s = "rat", t = "car"
#输出: false
############################# solution 1 #############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        for i in t:
            if i not in dic2:
                dic2[i] = 1
            else:
                dic2[i] += 1
        for i1, j1 in dic1.items():
            if i1 not in dic2.keys():
                return False
            if dic2[i1] != j1:
                return False
        for i1, j1 in dic2.items():
            if i1 not in dic1.keys():
                return False
            if dic1[i1] != j1:
                return False
        return True

############################# solution 2 #############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        for i in t:
            if i not in dic2:
                dic2[i] = 1
            else:
                dic2[i] += 1

        return dic1 == dic2

############################# solution 3 #############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for i in s:
            dic1[i] += 1
        for i in t:
            dic2[i] += 1
        return dic1 == dic2
############################# solution 4 #############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord("a")] += 1
        for i in range(len(t)):
            record[ord(t[i]) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False

        return True
