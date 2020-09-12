class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.numRows = numRows
        traingle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0] , row[-1] = 1,1
            for j in range(1, len(row)-1):
                row[j] = traingle[row_num-1][j-1] + traingle[row_num-1][j]
            traingle.append(row)
        return traingle
