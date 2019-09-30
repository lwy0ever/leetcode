class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        p = r'^(\d+)\.?(\d*)\(?(\d*)\)?$'
        i1,nr1,r1 = re.findall(p,S)[0]
        i2,nr2,r2 = re.findall(p,T)[0]
        if r1 == '':
            r1 = '0'
        if r2 == '':
            r2 = '0'
        print(i1,nr1,r1)
        print(i2,nr2,r2)
        #print(int(i1) * (10 ** len(nr1 + r1)) + int('0' + nr1) * (10 ** len(r1)) + int('0' + r1) - int(i1) * (10 ** len(nr1)) - int('0' + nr1),(10 ** len(nr2 + r2) - 10 ** len(nr2)))
        sval = (int(i1) * (10 ** len(nr1 + r1)) + int('0' + nr1) * (10 ** len(r1)) + int('0' + r1) - int(i1) * (10 ** len(nr1)) - int('0' + nr1)) * ((10 ** len(nr2 + r2) - 10 ** len(nr2)))
        tval = (int(i2) * (10 ** len(nr2 + r2)) + int('0' + nr2) * (10 ** len(r2)) + int('0' + r2) - int(i2) * (10 ** len(nr2)) - int('0' + nr2)) * ((10 ** len(nr1 + r1) - 10 ** len(nr1)))
        #print(sval,tval)
        return sval == tval