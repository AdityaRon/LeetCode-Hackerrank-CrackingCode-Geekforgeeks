class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        self.name = name
        self.typed = typed
        # i = 0
        # for j in range(len(typed)):
        #     if i < len(name) and typed[j] == name[i]:
        #         i+=1
        #     elif j == 0 or typed[j] != typed[j-1]:
        #         return False
        # return i == len(name)
    
        i = 0
        j = 0
        while (i <= len(typed)-1):
            if j <= len(name)-1 and typed[i] == name[j]:
                i+=1
                j+=1
            elif j == 0 or typed[i] != typed[i-1]:
                return False
            else:
                i+=1
        return j == len(name)
            
