class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remainder = target-nums[i]
            if remainder in hashmap.keys():
                return [i, hashmap[remainder]]
            else:
                hashmap[nums[i]] =i 