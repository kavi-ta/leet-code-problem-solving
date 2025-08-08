class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        min_len = min([len(i) for i in strs])
        low, high = 0 , min_len

        while(low<=high):
            mid = (low+high)//2
            prefix = strs[0][0:mid]
            if all(s.startswith(prefix) for s in strs):
                low = mid+1
            else:
                high = mid-1
        return strs[0][:high]

        
# NOTE: 
# 1. here the number of character comparison is reduced
# 2. the overhead for sorting is also reduced
