class Solution:
    def reverseVowels(self, s: str) -> str:
        self.s = s
        vowels = ['a', 'e', 'i', 'o', 'u']
        currentList = list(s)
        currentVowels = []
        for index, char in enumerate(currentList):
            if char.lower() in vowels:
                currentList[index] = '_'
                currentVowels.append(char)
        if len(currentVowels) > 0:
            maxIndex = len(currentVowels)-1
            for index, char in enumerate(currentList):
                if char == '_':
                    currentList[index] = currentVowels[maxIndex]
                    maxIndex -=1
            return ''.join(currentList)
        else:
            return s

