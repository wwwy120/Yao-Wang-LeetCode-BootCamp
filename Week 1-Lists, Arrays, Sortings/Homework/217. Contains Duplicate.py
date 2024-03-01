class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #Time Complexity: O(n)
        #Space Complexity: O(1)s
        return len(nums) != len(set(nums))

        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    return True
        return False
        """

        






        
