'''
合并两个有序数组
阿里一面
'''
# 题目中的条件两个有序整数数组，可以直接比较nums1和nums2元素的大小，
# 然后根据大小加入到nums1的末尾，最后还要考虑nums2的元素是否还有剩余即可。
# 二路归并问题

# 比nums1[0]大的都插在它的后面了，如果nums2还有剩余，那么肯定比它小，直接插在前面

def merge(self, nums1, m, nums2, n):
	while m > 0 and n > 0:
		if nums1[m-1] > nums2[n-1]:
			nums1[m+n-1] = nums1[m-1]
			m -= 1
		else:
			nums1[m+n-1] = nums2[n-1]
			n -= 1

	if n > 0:
		nums1[:n] = nums2[:n]
