# You are given a string word containing lowercase English letters.

# Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

# Return the minimum number of pushes needed to type word after remapping the keys.

# An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

class Solution:
    def minimumPushes(self, word: str) -> int:
        # a to z are assigned in an array with 0 frequencies to begin with
        frequency = [0] * 26
        totalPushes = 0
        # Update frequency of each character in the string based on ord calcuations. 
        # Assuming all the characters in the word are strings. 'a' should be at index 0 and 'z' should be at 25.
        for char in word:
            frequency[ord(char)-ord('a')] +=1
        # Sort by the desc order to get max push counts
        frequency.sort(reverse=True)
        print(frequency)
        # Loop for all characters in the word
        for i in range(26):
            if frequency[i] == 0:
                break
            # Since we have only 8 numbers available to be mapped to characters, we map them based on the frequency.
            totalPushes += (i//8 + 1) * (frequency[i])
        return totalPushes
        
