class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        occ = Counter(s1)
        i = 0
        j = len(s1) - 1
        while j <= len(s2):
            substr = Counter(s2[i:j+1])
            print(occ, substr)
            if occ == substr:
                return True
            i += 1
            j += 1
        return False

