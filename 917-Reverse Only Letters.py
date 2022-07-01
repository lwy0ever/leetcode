class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # 双指针
        n = len(s)
        arr = list(s)
        l = 0
        r = n - 1
        while l < r:
            while l < r and not arr[l].isalpha():
                l += 1
            while l < r and not arr[r].isalpha():
                r -= 1
            if l < r:
                arr[l],arr[r] = arr[r],arr[l]
                l += 1
                r -= 1
            else:
                break
        return ''.join(arr)