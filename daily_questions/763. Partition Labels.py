"""

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]

https://leetcode.com/problems/partition-labels/editorial

"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #create a dictionary of store last indexes
        last_index = {}
        partitionStart = 0
        partitionEnd = 0
        parititonSizes = []
        for index, char in enumerate(s):
            last_index[char] = index
        for index, char in enumerate(s):
            partitionEnd = max(partitionEnd, last_index[char])
            if index == partitionEnd:
                parititonSizes.append(index - partitionStart + 1)
                partitionStart = index + 1
        return parititonSizes
