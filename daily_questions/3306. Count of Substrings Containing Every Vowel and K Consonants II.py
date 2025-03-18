"""
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
"""

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        self.word = word
        self.k = k
        def isVowel(char):
            return char in ["a", "e", "i", "o", "u"]
        def atleastK(word, k):
            valid_sub_string = 0
            start = 0
            end = 0
            vowelCount = {}
            consonants = 0

            while end < len(word):
                new_letter = word[end]

                if isVowel(new_letter):
                    vowelCount[new_letter] = vowelCount.get(new_letter, 0) + 1
                else:
                    consonants +=1
                while len(vowelCount) == 5 and consonants >= k:
                     valid_sub_string += len(word)-end
                     start_letter = word[start]
                     if isVowel(start_letter):
                        vowelCount[start_letter] = vowelCount.get(start_letter) - 1
                        if vowelCount[start_letter] == 0:
                            vowelCount.pop(start_letter)
                     else:
                        consonants -= 1
                     start += 1
                end += 1
            return valid_sub_string

        return atleastK(word, k) - atleastK(word, k+1)






        

        
