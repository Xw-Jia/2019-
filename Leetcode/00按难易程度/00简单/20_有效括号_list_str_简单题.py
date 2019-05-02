'''
20-有效括号-简单题

给定一个只包含字符'('，')'，'{'，'}'，'['和']'的字符串，判断输入字符串是否有效。
括号必须按正确的顺序关闭，“()”和“()[]{}”都是有效的，但是“()”和“([)]”不是有效的。
'''

class Solution(object):
	def isValid(self, s):
		'''
		:type s: str
		:rtype: bool
		'''
		stack = []
		d = ['()', '[]', '{}']
		for i in range(len(s)):
			stack.append(s[i])
			if len(stack) >= 2 and stack[-2] + stack[-1] in d:
				stack.pop()
				stack.pop()
		return len(stack) == 0