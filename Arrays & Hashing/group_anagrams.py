class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for str in strs:
            sortedstr=sorted(str)
            key=tuple(sortedstr)
            if key not in result:
                result[key]=[str]
            else:
                result[key].append(str)
        return result.values()