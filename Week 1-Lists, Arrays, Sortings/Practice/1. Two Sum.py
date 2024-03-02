class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #1. Brute Approach
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res += [i, j]
        return res
        
        #2. Two Pointers Approach
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        sort = []
        for i in range(len(nums)):
            sort += [nums[i]]
        sort.sort()

        left, right = 0, len(sort) - 1
        res = []
        while left != right:
            if sort[left] + sort[right] == target:
                break
            elif sort[left] + sort[right] < target:
                left += 1
            else:
                right -= 1
        index1 = nums.index(sort[left])
        nums[index1] = 10**9 + 1
        index2 = nums.index(sort[right])
        res += [index1, index2]
        return res
