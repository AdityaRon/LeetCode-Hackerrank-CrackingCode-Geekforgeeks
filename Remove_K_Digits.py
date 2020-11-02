class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        self.num = num
        self.k = k
        # if len(num) == k:
        #     return '0'
        # for i in range(k):
        #     j = 0
        #     while (j < len(num)-1 and int(num[j]) <= int(num[j+1])):
        #         j+=1
        #     num = num[:j] + num[(j+1):]
        # print(num[0])
        # while(len(num) > 0 and num[0] == '0'):
        #     num = num[1:]
        # return num if len(num) > 0 else "0"
        stack = []
        for i in num:
            while stack and k > 0 and stack[-1] > i:
                k-=1
                stack.pop()
            stack.append(i)
        while stack and k > 0:
            stack.pop()
            k-=1
        if len(stack) == 0:
            return '0'
        return str(int(''.join(stack)))
