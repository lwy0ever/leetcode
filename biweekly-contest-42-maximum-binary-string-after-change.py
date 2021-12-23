class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # 如果是00,替换成10
        # 如果是10,并且前面有0,替换成01并回溯——会超时
        #   也就意味着,将0111...1110,变为00111...111
        #   记录0出现的位置——还是会超时
        # 继续观察,00111...111还可以变成10111...111
        # 也就是说,当第2次出现0的时候,0可以被合并为一个,并且0的位置在第一次出现的位置后移1位
        n = len(binary)
        # 再优化下面的循环
        cnt = binary.count('0')
        if cnt > 0:
            pre0ind = binary.find('0')
            pre0ind += cnt - 1
            return '1' * (pre0ind) + '0' + '1' * (n - pre0ind - 1)
        else:
            return binary
        '''
        pre0ind = -1
        for i in range(n):
            if binary[i] == '0':
                if pre0ind >= 0:
                    pre0ind += 1
                else:
                    pre0ind = i
        return '1' * (pre0ind) + '0' + '1' * (n - pre0ind - 1) if pre0ind >= 0 else binary
        '''

        '''
        #####
        # 改进想法
        # 如果是00,替换成10
        # 如果是10,并且前面有0,替换成01并回溯——会超时
        #   也就意味着,将0111...1110,变为00111...111
        #   记录0出现的位置——还是会超时
        n = len(binary)
        arr = list(binary)
        ind = 0
        pre0ind = -1
        while ind < n - 1:
            if arr[ind] == '0' and arr[ind + 1] == '0':
                arr[ind] = '1'
                pre0ind = ind
                ind += 1
            elif arr[ind] == '1' and arr[ind + 1] == '0':
                if pre0ind >= 0:
                    arr[ind + 1] = '1'
                    arr[pre0ind + 1] = '0'
                    ind = pre0ind
                    pre0ind = -1
                else:
                    ind += 1
            else:
                if arr[ind] == '0':
                    pre0ind = ind
                ind += 1
            #print(arr,ind,pre0ind)
        return ''.join(arr)

        #####
        # 最初想法
        # 如果是00,替换成10
        # 如果是10,并且前面有0,替换成01并回溯
        # 会超时
        n = len(binary)
        arr = list(binary)
        ind = 0
        pre0 = False
        while ind < n - 1:
            if arr[ind] == '0' and arr[ind + 1] == '0':
                arr[ind] = '1'
                pre0 = True
                ind += 1
            elif arr[ind] == '1' and arr[ind + 1] == '0':
                if pre0 == True:
                    arr[ind] = '0'
                    arr[ind + 1] = '1'
                    ind -= 1
                else:
                    pre0 = False
                    ind += 1
            else:
                if arr[ind] == '0':
                    pre0 = True
                ind += 1
            #print(arr,ind,pre0)
        return ''.join(arr)
        '''