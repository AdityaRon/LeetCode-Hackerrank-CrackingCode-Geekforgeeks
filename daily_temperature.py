class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        self.T = T
        result = [0]*len(T)
#         for i,j in enumerate(T):
#             count = 0
#             for l in T[i+1:]:
#                 if j < l:
#                     result[i] = count+1
#                     break  
#                 else:
#                     count+=1         
#         return result
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                cur = stack.pop()
                result[cur] = i - cur
            stack.append(i)
        return result
        
