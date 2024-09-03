class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # nums.sort()
        # minimum = 0

        # for i in range(1, len(nums)):
        #     if nums[i] <= nums[i-1]:
        #         increment = nums[i-1] + 1 - nums[i]
        #         minimum += increment

        #         nums[i] = nums[i-1] + 1
        
        # return minimum
        n = len(nums)
        max_val = max(nums)
        min_increments = 0

        # Create a frequencyCount array to store the frequency of each value in nums
        frequency_count = [0] * (n + max_val + 1)

        # Populate frequencyCount array with the frequency of each value in nums
        for val in nums:
            frequency_count[val] += 1

        # Iterate over the frequencyCount array to make all values unique
        for i in range(len(frequency_count)):
            if frequency_count[i] <= 1:
                continue

            # Determine excess occurrences, carry them over to the next value,
            # ensure single occurrence for current value, and update min_increments.
            duplicates = frequency_count[i] - 1
            frequency_count[i + 1] += duplicates
            frequency_count[i] = 1
            min_increments += duplicates

        return min_increments