class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(',')
        n = len(arr)
        #print(arr)
        
        ind = 0
        need = 1
        while ind < n and need > 0:
            if arr[ind] != '#': # 每增加一个非None节点,则必然跟随2个子节点
                need += 2
            ind += 1    # 观察位后移
            need -= 1   # 当前节点已满足之前的需求,需求减少1
        return need == 0 and ind == n   # 全部满足 and 观察完毕
                