#给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
#(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
#示例 1：
#输入：ransomNote = "a", magazine = "b"
#输出：false
#示例 2：
#输入：ransomNote = "aa", magazine = "ab"
#输出：false
#示例 3：
#输入：ransomNote = "aa", magazine = "aab"
#输出：true
###################### solution 1 ######################
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ra = []
        ma = []
        for i in ransomNote:
            ra.append(i)
        for i in magazine:
            ma.append(i)
        while ra:
            for i in ra:
                if i in ma:
                    ra.remove(i)
                    ma.remove(i)
                else:
                    return False
        if ra == []:
            return True
        return False

###################### solution 2 ######################
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for i in magazine:
            arr[ord(i) - ord("a")] += 1
        for i in ransomNote:
            if arr[ord(i) - ord("a")] == 0:
                return False
            else:
                arr[ord(i) - ord("a")] -= 1
        return True
