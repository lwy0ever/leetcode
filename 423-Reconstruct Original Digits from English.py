class Solution:
    def originalDigits(self, s: str) -> str:
        # zero
        # one
        # two
        # three
        # four
        # five
        # six
        # seven
        # eight
        # nine
        # cnt = collections.Counter('zeroonetwothreefourfivesixseveneightnine')
        '''
        cnt:{
            'e': 9,
            'o': 4, # zero,two,four...one
            'n': 4, # nine,seven...one
            'i': 4, # five,six,eight...nine
            'r': 3, # three,four,zero
            't': 3, # two,three,eight
            'h': 2, # eight...three
            'f': 2, # four...five
            'v': 2,
            's': 2, # six...seven
            'z': 1, # zero
            'w': 1, # two
            'u': 1, # four
            'x': 1, # six
            'g': 1} # eight
        '''
        cnt = collections.Counter(s)
        ans = [0] * 10  # ans[i]表示i的个数
        ans[8] = cnt['g']
        cnt['i'] -= cnt['g']
        cnt['h'] -= cnt['g']
        ans[6] = cnt['x']
        cnt['s'] -= cnt['x']
        cnt['i'] -= cnt['x']
        ans[4] = cnt['u']
        cnt['f'] -= cnt['u']
        cnt['o'] -= cnt['u']
        ans[2] = cnt['w']
        cnt['o'] -= cnt['w']
        ans[0] = cnt['z']
        cnt['o'] -= cnt['z']
        ans[7] = cnt['s']
        ans[5] = cnt['f']
        cnt['i'] -= cnt['f']
        ans[3] = cnt['h']
        ans[9] = cnt['i']
        ans[1] = cnt['o']
        return ''.join([str(i) * ans[i] for i in range(10)])