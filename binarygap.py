import re
import sys

class binaryGap():
    def __init__(self, test):
        self.test = bin(int(test))[2:]

    def checkGap(self):
        c = map((lambda x:x.start()), re.finditer('1', self.test))
        d = map((lambda x:len(re.findall('0', x))), map((lambda x:self.test[x[0]:x[1]+1]), map((lambda x:c[x:x+2]), range(len(c)-1))))
        if(d):
            return max(d)
        else:
            return 0


    def printTest(self):
        print self.test


if __name__ == "__main__":
     b = binaryGap(sys.argv[1])
     print b.checkGap()
     #b.printTest()
