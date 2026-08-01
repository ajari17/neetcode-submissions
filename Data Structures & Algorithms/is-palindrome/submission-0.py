class Solution:
    def isPalindrome(self, s: str) -> bool:
        return re.sub(r'[^a-zA-Z0-9]', '', (s[::-1].lower())) == re.sub(r'[^a-zA-Z0-9]', '', (s[::-1].lower()))[::-1]
        