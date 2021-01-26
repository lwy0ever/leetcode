class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        firstNum = dict()
        for p in pieces:
            firstNum[p[0]] = p
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] not in firstNum:
                return False
            for p in firstNum[arr[i]]:
                if p == arr[i]:
                    i += 1
                else:
                    return False
        return True
        '''
        i = 0
        n = len(arr)
        while i < n:
            ind = -1
            m = len(pieces)
            for j in range(m):
                if pieces[j][0] == arr[i]:
                    ind = j
                    break
            else:
                return False
            if ind == -1:
                return False
            for b in pieces[j]:
                if b == arr[i]:
                    i += 1
                else:
                    return False
            pieces.pop(ind)
            #print(i,pieces)
        return True
        '''