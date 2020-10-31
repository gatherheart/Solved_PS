class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, n1 in enumerate(nums):
            n2 = target - n1
            if not n1 in cache:
                cache[n2] = i
            else:
                return [cache[n1], i]
