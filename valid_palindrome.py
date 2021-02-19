class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validate(left,right,s,deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return validate(left+1, right, s, True) or validate(left, right-1,s, True)
                else:
                    left +=1
                    right -=1
            return True
        return validate(0, len(s)-1, s, False)
        
