class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        self.temperatures = temperatures
        # result = []
        # for index, temp in enumerate(temperatures):
        #     count = 0
        #     match = False
        #     for nexttemp in temperatures[index+1 :]:
        #         if nexttemp - temp > 0:
        #             count += 1
        #             match = True
        #             result.append(count)
        #             break
        #         else:
        #             count += 1
        #     if count >= 1 and not match:
        #         result.append(0)
        # if count == 0 or not match:
        #     result.append(0)
        # return result
        stack = []
        result = [0]*len(temperatures)
        for index, current_temp in enumerate(temperatures):
            while stack and current_temp - temperatures[stack[-1]] > 0:
                previous = stack.pop()
                result[previous] = (index-previous)
            stack.append(index)
            #print(index, current_temp, stack, result)
        return result
