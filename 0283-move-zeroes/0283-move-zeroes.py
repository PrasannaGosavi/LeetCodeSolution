class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1