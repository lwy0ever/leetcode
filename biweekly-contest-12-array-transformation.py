class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        while True:
            toadd = []
            tominus = []
            for i in range(1,n - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    toadd.append(i)
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    tominus.append(i)
            if toadd or tominus:
                for i in toadd:
                    arr[i] += 1
                for i in tominus:
                    arr[i] -= 1
            else:
                break
        return arr
                