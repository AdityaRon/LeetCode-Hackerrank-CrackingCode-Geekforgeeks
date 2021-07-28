class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.bills = bills
        changeFive = 0
        changeTen = 0
        for i in bills:
            if i == 5:
                changeFive +=1
            elif i == 10:
                changeFive -=1
                changeTen +=1
            elif changeTen > 0:
                changeTen -= 1
                changeFive -=1
            else:
                changeFive -=3
            if changeFive < 0:
                return False
        return True
                
            
        
