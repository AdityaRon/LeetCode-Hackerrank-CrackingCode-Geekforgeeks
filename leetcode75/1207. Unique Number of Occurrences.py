class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = {}
        unique = []
        for value in arr:
            if value in occurence:
                occurence[value] += 1
            else:
                occurence[value] = 0
        for value in occurence.values():
            if value not in unique:
                unique.append(value)
            else:
                return False
        return True
        
