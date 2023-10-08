class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        whether = list(set(nums))
        if (len(whether) != len(nums)):
            return True
        else:
            return False    
