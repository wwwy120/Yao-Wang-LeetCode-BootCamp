class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i] = len(nums) + 1
        
        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums):
                nums[abs(nums[i]) - 1] = - abs(nums[nums[i] - 1])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1

        #Time Complexity: O(n)
        #Space Complexity: O(n)
        d_nums = {}
        maximum = 0
        for n in nums:
            if n > maximum:
                maximum = n
            if n > 0:
                d_nums[n] = d_nums.get(n, 1)
        
        d_all = {}
        for i in range(1, maximum):
            d_all[i] = d_nums.get(i, 0)
            if d_all[i] == 0:
                return i
        
        return maximum + 1
