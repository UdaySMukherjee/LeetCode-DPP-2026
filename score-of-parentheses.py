class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return eval(s.replace('()', '+1').replace('(', '+2*('))
