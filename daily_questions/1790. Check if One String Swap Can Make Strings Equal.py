""" You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1Set = set(list(s1))
        s2Set = set(list(s2))
        for char in s1Set:
            if char not in s2Set:
                return False
        count = 0
        firstIndex = 0
        secondIndex = 0
        for index, char in enumerate(s1):
            if char != s2[index]:
                count += 1
                if count > 2:
                    return False
                elif count == 1:
                    firstIndex = index
                else:
                    secondIndex = index
        return (s1[firstIndex] == s2[secondIndex] and s1[secondIndex] == s2[firstIndex])

        
