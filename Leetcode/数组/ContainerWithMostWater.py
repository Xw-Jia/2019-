'''
https://leetcode.com/problems/container-with-most-water/description/
Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
给一组数据，返回两组边界中可盛放水最多的一组。
'''

'''
思路：
从两边两个指针向中间靠拢，移动较小的那个对应的指针：
如果移动之后，x1 < x0,肯定变小，如果 x1>x0，需要比较min(x,y)*distance 与原来的值
继续移动，直到头尾相遇
复杂度为：时间 O(n)   空间：O(1)
'''
class Solution(Object):
