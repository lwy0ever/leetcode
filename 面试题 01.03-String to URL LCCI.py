class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return '%20'.join(S[:length].split(' '))