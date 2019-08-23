class Solution():
    def prmax(self,num):
        num_list = [0] * num
        for i in range(10):
            num_list[0] = str(i)
            self.ff(num_list,num,0)

    def prettypr(self, number):  # 输出数字
        # 此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
        isBeginning0 = True
        nLength = len(number)
        for i in range(nLength):
            if isBeginning0 and number[i] != '0':  # 只输出非零项
                isBeginning0 = False
            if not isBeginning0:
                print('%c' % number[i],end='')
        print('\t')

    def ff(self,num,length,index):
        if index == length-1:
            self.prettypr(num)
            return
        for i in range(10):
            num[index+1] = str(i)
            self.ff(num,length,index+1)

if __name__ == '__main__':
    Solution().prmax(3)