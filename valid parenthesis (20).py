# Valid parenthesis No.20
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
"""

class Parenthesis:
    def __init__(self, item):
        """
        Attempt on 2019/12/18
        main idea: the base case is defined as when 2 consecutive elements form a matching pair of
        parenthesis. Use recursion.
        parenthesis_type includes parentheses '()', brackets '[]' & braces '{}'
        :param parenthesis_type: parentheses '()', brackets '[]' & braces '{}'
        :param direction: open bracket '(' and close bracket ')'
        """
        if item == '(' or ')':
            self.parenthesis_type = 'parentheses'
        elif item == '[' or ']':
            self.parenthesis_type = 'bracket'
        elif item == '{' or '}':
            self.parenthesis_type = 'brace'
        if item == '(' or '[' or '{':
            self.direction = 'open'
        elif item == ')' or ']' or '}':
            self.direction = 'close'



x = Parenthesis('(')
#print(help(Parenthesis))
print(x.parenthesis_type)
print(x.direction)
