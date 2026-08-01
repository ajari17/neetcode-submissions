class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return re.sub(r'[^a-zA-Z0-9]', '', (s[::-1].lower())) == re.sub(r'[^a-zA-Z0-9]', '', (s[::-1].lower()))[::-1]
        s2 = ""
        for char in s:
            if(char.isalnum() == False) or char == " ":
                continue
            else:
                s2 += char
        s2 = s2.lower()

        return s2 == s2[::-1]
        