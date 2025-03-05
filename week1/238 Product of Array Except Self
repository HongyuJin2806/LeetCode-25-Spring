class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n

        pre_product = 1
        for i in range(0, n):
            output[i] *= pre_product
            pre_product *= nums[i]
            
        after_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= after_product
            after_product *= nums[i]

        return output