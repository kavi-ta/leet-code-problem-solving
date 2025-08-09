class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        write_pointer = 1
 
        for i in range(1,len(nums)):
           if nums[i]!=nums[i-1]:
            nums[write_pointer] = nums[i]
            write_pointer+=1

        return write_pointer