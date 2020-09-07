class Solution:
    def validIPAddress(self, IP: str) -> str:
        def checkV4(arr):
            if len(arr) != 4:
                return False
            for a in arr:
                if not a:
                    return False
                if len(a) > 1 and a[0] == '0':
                    return False
                l = 0
                for c in a:
                    if ord('0') <= ord(c) <= ord('9'):
                        l += 1
                    else:
                        return False
                if l <= 0 or l > 3 or int(a) >= 256:
                    return False                    
            return True
        
        def checkV6(arr):
            cnt = 0
            for a in arr:
                if not a:
                    return False
                l = 0
                for c in a.lower():
                    if ord('a') <= ord(c) <= ord('f') or ord('0') <= ord(c) <= ord('9'):
                        l += 1
                    else:
                        return False
                #print(l)
                if 1 <= l <= 4:
                    cnt += 1
            #print(cnt)
            return cnt == 8
        
        if ('.' in IP and ':' in IP) or ('.' not in IP and ':' not in IP):
            return 'Neither'
        if '.' in IP and checkV4(IP.split('.')):
            return 'IPv4'
        elif ':' in IP and checkV6(IP.split(':')):
            return 'IPv6'
        return 'Neither'