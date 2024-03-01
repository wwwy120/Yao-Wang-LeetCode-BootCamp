class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        n0 = 0
        n1 = 0
        n2 = len(nums) - 1

        while n1 <= n2:
            if nums[n1] == 0:
                nums[n1], nums[n0] = nums[n0], nums[n1]
                n0 += 1
                n1 += 1
            elif nums[n1] == 1:
                n1 += 1
            else:
                nums[n1], nums[n2] = nums[n2], nums[n1]
                n2 -= 1
