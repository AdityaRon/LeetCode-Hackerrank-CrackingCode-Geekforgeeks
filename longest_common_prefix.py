class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.strs = strs
        result = strs[0] if len(strs) >= 1 else ""
        i = 1
        prefix = ''
        while i <= len(strs)-1:
            for k,m in zip(result,strs[i]):
                if k == m:
                    prefix += k
                else:
                    break
            result = prefix
            prefix = ''
            i+=1
        return (result)
                
            
         
                    
            
        
