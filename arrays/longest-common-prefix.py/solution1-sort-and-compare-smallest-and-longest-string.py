class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        # lexicographically sorts the string
        strs = sorted(strs)
        # consider smallest_str as the longest_prefix
        smallest_str, longest_str = strs[0], strs[-1]
        j =0
        while(j<len(smallest_str)):
            if smallest_str[j]==longest_str[j]:
                j+=1
            else:
                return smallest_str[:j]
        return smallest_str

        