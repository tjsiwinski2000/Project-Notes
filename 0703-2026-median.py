# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/2056324837/
# 0704-2026 
# TJS: Honestly I didn't think my code was that good 
# - BUT it had Runtime 0ms and Memory 12.42MB on one run beat 85.55%

class Solution(object):       
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        main_list =sorted(nums1 + nums2)
        length = len(main_list)
        print(f'length:{length}')
        if length %2 ==0:
            #even number of items
            t1 = int(length/2)-1
            t2 = int(length/2 ) 
            print(f'temp1:{t1} \t temp2:{t2}')
            return  float((main_list[t1] + main_list[t2])*.5)
        else:
            #odd number of items
            temp= (length //2) 
            print(f'ood temp = {temp}')
            return float(main_list[temp])
            
            
       
    
# nums1 = [1,2]
# nums2 = [3,4]
# nums1 = [1,3]
# nums2 = [2]
nums1 =[]
nums2 =[2,3]
my_object = Solution()
print(my_object.findMedianSortedArrays(nums1=nums1,nums2=nums2))
