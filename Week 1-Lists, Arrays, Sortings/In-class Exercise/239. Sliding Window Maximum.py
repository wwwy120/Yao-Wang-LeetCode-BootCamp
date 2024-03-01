class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_lst = []
        for i in range(len(nums) - k + 1):
            max_lst += [max(nums[i:i+k])]
        return max_lst



        
