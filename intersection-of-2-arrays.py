"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""
def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection_list = []
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i] == nums2[j]:
                    nums2[j] = -1
                    intersection_list.append(nums1[i])
                    break
        return intersection_list
