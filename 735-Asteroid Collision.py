class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []  # stack[i] > 0
        for a in asteroids:
            if a < 0:
                if not stack:
                    ans.append(a)
                else:
                    while stack:
                        if stack[-1] + a > 0:   # a will explode 
                            break
                        elif stack[-1] + a == 0:    # a and stack[-1] both will explode
                            stack.pop()
                            break
                        else:
                            stack.pop()
                    else:   # all stack[i] exploded,a is alive
                        ans.append(a)
            else:
                stack.append(a)
        for a in stack:
            ans.append(a)
        return ans
            