"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
"""

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True if len(s) - len(set(s)) >= 1 else False
        
        count = 0
        firstIndex = 0
        secondIndex = 0
        for index, char in enumerate(s):
            #print(char, goal[index])
            if char != goal[index]:
                count += 1
                if count > 2:
                    return False
                elif count == 1:
                    firstIndex = index
                else:
                    secondIndex = index
        # if count != 2:
        #     return False
        #print(count)
        return s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]
           
