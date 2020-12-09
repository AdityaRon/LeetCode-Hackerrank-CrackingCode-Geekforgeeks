class Solution:
    def maximum69Number (self, num: int) -> int:
        self.num = num
        changes = list(str(num))
        result = num
        i = 0
        while i <= len(changes)-1:
            temp = changes[i]
            changes[i] = '9'  
            result = max(result, int(''.join(changes)))
            print(result)
            changes[i] = temp
            i+=1
        return result
            
        
