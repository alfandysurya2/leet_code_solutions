class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        n = len(nums)
        
        for i in range(0, n, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

        return nums
            
            
        