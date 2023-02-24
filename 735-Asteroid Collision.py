class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 栈
        ans = list()
        for a in asteroids:
            addA = True
            if a < 0:
                while ans:
                    if ans[-1] > 0:
                        if ans[-1] + a < 0:
                            ans.pop()
                        elif ans[-1] + a == 0:
                            ans.pop()
                            addA = False
                            break
                        else:
                            addA = False
                            break
                    else:
                        break
            if addA:
                ans.append(a)
            #print(ans)
        return ans