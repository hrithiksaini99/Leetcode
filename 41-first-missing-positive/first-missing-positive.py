class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        def swap(i,j):
            nums[i],nums[j] = nums[j],nums[i]
         # Place each positive integer i at index i-1 if possible
        for i in range(n):
            while 0 < nums[i] <=n and nums[i] != nums[nums[i]-1]:
                swap(i, nums[i]-1)
         # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        # If all positive integers from 1 to n are present, return n + 1
        return n+1 