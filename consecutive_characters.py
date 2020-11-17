class Solution:
    def maxPower(self, s: str) -> int:
        self.s = s
        result = ''
        temp = s[0]
        count = 1
        length = 1
        for i in s[1:]:
            if i == temp:
                result += i
                count += 1
                length = max(length,count)
                temp = i
            else:
                result = ''
                count = 1
                temp = i
        return length
        #return max(len(list(b)) for a, b in itertools.groupby(s))
