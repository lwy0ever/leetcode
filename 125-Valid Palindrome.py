class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
        return True
        '''
        s = ''.join(re.findall(r'\w', s)).lower()
        #print(s)
        return s == s[::-1]
        '''