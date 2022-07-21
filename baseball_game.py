class Solution:
    def calPoints(self, ops: List[str]) -> int:
        self.ops = ops
        results = []
        for i in ops:
            #print(results)
            temp = results[-1] if len(results) > 0 else 0 
            if i == 'C':
                results.pop()
            elif i == 'D':
                results.append(temp*2)
            elif i == '+':
                temp += results[-2]
                results.append(temp)
            else:
                results.append(int(i))
        return sum(results)
            
