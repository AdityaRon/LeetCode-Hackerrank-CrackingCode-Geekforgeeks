class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        # results = {'2':['a','b','c'],
        #            '3':['d','e','f'],
        #            '4':['g','h','i'],
        #            '5':['j','k','l'],
        #            '6':['m','n','o'],
        #            '7':['p','q','r','s'],
        #            '8':['t','u','v'],
        #            '9':['w','x','y','z']}
        # combs = []
        # if len(digits) == 0:
        #     return []
        # elif len(digits) == 1:
        #     return results[digits]
        # else:
        #     mappings = [results[digits[i]] for i in range(0,len(digits))]
        #     if len(mappings) == 2:
        #         for i in mappings[0]:
        #             for j in mappings[1]:
        #                 combs.append(i+j)
        #     elif len(mappings) == 3:
        #         for i in mappings[0]:
        #             for j in mappings[1]:
        #                 for k in mappings[2]:
        #                     combs.append(i+j+k)
        #     else:
        #         for i in mappings[0]:
        #             for j in mappings[1]:
        #                 for k in mappings[2]:
        #                     for l in mappings[3]:
        #                         combs.append(i+j+k+l)
        #     return combs
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for idx in range(len(digits)):
            # for l in digit_map[digits[idx]]:
            #      for prev in result:
            #         print(l,prev)
            #         result.append(prev+l)
            result = [prev + l for prev in result for l in digit_map[digits[idx]]]
        return result
                
                
            
        
        
