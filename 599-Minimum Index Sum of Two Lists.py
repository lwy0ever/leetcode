class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # 利用hash
        dict1 = {s:i for i,s in enumerate(list1)}
        minIndexSum = float('inf')
        for i,s in enumerate(list2):
            if s in dict1:
                if dict1[s] + i < minIndexSum:
                    ans = [s]
                    minIndexSum = dict1[s] + i
                elif dict1[s] + i == minIndexSum:
                    ans.append(s)
        return ans
        
        # 双循环
        n1 = len(list1)
        n2 = len(list2)
        ans = []
        for indexSum in range(n1 + n2 - 1):
            for index1 in range(min(indexSum,n1 - 1),-1,-1):
                #print(indexSum,index1)
                index2 = indexSum - index1
                if index2 < 0 or index2 >= n2:
                    break
                if list1[index1] == list2[index2]:
                    ans.append(list1[index1])
            if ans:
                return ans