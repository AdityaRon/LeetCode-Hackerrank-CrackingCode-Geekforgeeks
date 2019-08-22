class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        self.A = A
        start = set(A[0])
        results = []
        for char in start:
            min_occ = min([word.count(char) for word in A])
            if min_occ > 0:
                results += min_occ * [char]
        return (results)
