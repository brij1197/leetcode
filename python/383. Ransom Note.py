class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for _ in set(ransomNote):
            if ransomNote.count(_)>magazine.count(_):
                return False
        return True