class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        MAXWIDTH = 100
        line = 1
        width = 0
        base = ord('a')
        for c in s:
            w = widths[ord(c) - base]
            if width + w > MAXWIDTH:
                line += 1
                width = w
            else:
                width += w
        return [line,width]