class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        self.A = A
        rows = len(A)
        cols = len(A[0])
        result = []
        for i in range(cols):
            tmp = []
            for j in range(rows):
                tmp.append(A[j][i])
            result.append(tmp)
        return result
