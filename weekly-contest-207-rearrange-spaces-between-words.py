class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        arr = text.split()
        m = sum(len(a) for a in arr)
        if len(arr) == 1:
            return arr[0] + ' ' * (n - m)
        d,mod = divmod(n - m,len(arr) - 1)
        return (' ' * d).join(arr) + ' ' * mod