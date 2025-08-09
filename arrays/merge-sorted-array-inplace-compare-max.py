class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        write_index = m+n-1
        i = m-1
        j = n-1
        while(write_index>=0 and j>=0 and i>=0):

            if nums1[i]>nums2[j]:
                nums1[write_index] = nums1[i]
                i-=1  
            else:
                nums1[write_index] = nums2[j]
                j-=1
            write_index -=1
        if j>=0:
            # elements are remaining in nums2
            nums1[:write_index+1] = nums2[:j+1]