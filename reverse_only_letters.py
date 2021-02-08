class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        self.S = S
        originalString = list(S)
        # updateString = []
        # for i in S:
        #     if i.isalpha():
        #         updateString.append(i)
        # updateString = updateString[::-1]
        # j = 0
        # for i in range(len(originalString)):
        #     if originalString[i].isalpha():
        #         originalString[i] = updateString[j]
        #         j+=1
        # return ''.join(originalString)
            
        start ,end = 0, len(originalString)-1
        while start < end:
            if not originalString[start].isalpha():
                start+=1
            elif not originalString[end].isalpha():
                end-=1
            else:
                temp = originalString[start]
                originalString[start] = originalString[end]
                originalString[end] = temp
                start+=1
                end-=1
        return ''.join(originalString)
        
