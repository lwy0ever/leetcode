class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ps = path.split('/')
        for p in ps:
            if p == '' or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)