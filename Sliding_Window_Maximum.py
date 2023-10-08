class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        # only need to check one value, if the 
        for i in range(len(nums)):
            if (i+k) <= len(nums):
                arr.append(max(nums[i:(i+k)]))
        return arr
