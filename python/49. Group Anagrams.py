class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for string in strs:
            sorted_str=sorted(string)
            key=tuple(sorted_str)
            if key not in result:
                result[key]=[string]
            else:
                result[key].append(string)
        return result.values()