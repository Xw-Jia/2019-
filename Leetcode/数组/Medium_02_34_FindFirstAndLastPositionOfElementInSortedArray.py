'''
给定一个按升序排序的整数数组，找出给定目标值的起始和结束位置。您的算法的运行时复杂度必须是O(log n)的顺序。如果在数组中没有找到目标，返回[- 1,1]。
'''
'''
要求： 时间复杂度必须是 O(log n)
看到log n 立马先想到二分，排好序的数组，刚好可以利用二分。
'''

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums ==[] :
            return [-1,-1]
        
        if target >=nums[0]and target <=nums[-1]:
 
            mid = 0
            l  = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r) // 2            
                if target == nums[mid]:
                    print(mid)
                    l = mid
                    r = mid
                    while l-1>=0 and nums [l-1] == nums[l]:
                        l -= 1
                        print(l)
                        
                    while r+1<=len(nums)-1 and nums [r] == nums[r+1]:
                        r +=1
                    return [l,r]
                if nums[mid] < target:
                    l = mid +1
                else :
                    r = mid -1
        return [-1,-1]
'''
思路很好玩，再尝试一下
'''
