'''
如果用double for loop，时间复杂度会超过限制
先求出A和B之间的差别的一半，diff
不需要考虑重复的element，所以可以把A变成set
循环B中的元素b，如果b+diff在A中，说明把这个元素加进B，能把B凑成总和一半
'''

def fairCandySwAP(self, A, B):
	diff = (sum(A) - sum(B)) // 2
	A = set(A)
	B = set(B)
	for b in B:
		if diff + b in A:
			return [b+diff, b]
