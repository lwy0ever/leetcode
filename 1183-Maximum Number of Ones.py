class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        # 优先堆积最长边剩余的空间
        ans = 0
        maxside = max(width,height)
        minside = min(width,height)
        maxline,maxremain = divmod(maxside,sideLength)
        minline,minremain = divmod(minside,sideLength)
        ans += maxline * minline * maxOnes
        if minremain * maxremain >= maxOnes:
            ans += maxOnes * (maxline + minline + 1)
            return ans
        else:
            ans += (maxremain * minremain) * (maxline + minline + 1)
            #print((maxremain * minremain) * (maxline + minline + 1))
            if minremain * sideLength >= maxOnes:
                ans += (maxOnes - maxremain * minremain) * maxline
                return ans
            else:
                ans += ((sideLength - maxremain) * minremain) * maxline
                #print(((sideLength - maxremain) * minremain) * maxline)
                if maxOnes - minremain * sideLength >= (sideLength - minremain) * maxremain:
                    ans += (sideLength - minremain) * maxremain * minline
                    #print((sideLength - minremain) * maxremain * minline)
                    return ans
                else:
                    ans += (maxOnes - sideLength * minremain) * minline
                    return ans
