#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#有效字符串需满足：
#左括号必须用相同类型的右括号闭合。
#左括号必须以正确的顺序闭合。
#示例 1：
#输入：s = "()"
#输出：true
#示例 2：
#输入：s = "()[]{}"
#输出：true
#示例 3：
#输入：s = "(]"
#输出：false
#示例 4：
#输入：s = "([)]"
#输出：false
#示例 5：
#输入：s = "{[]}"
#输出：true
################## solution 1 ##################
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
                
        if not stack:
            return True
        else:
            return False
        
################## solution 2 ##################
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item: 
                return False
            else: 
                stack.pop()
        if not stack:
            return True 
        else: 
            return False
