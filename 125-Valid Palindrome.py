class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r'\w', s)).lower()
        #print(s)
        return s == s[::-1]