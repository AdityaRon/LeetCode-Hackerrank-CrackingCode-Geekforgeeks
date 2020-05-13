def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(i,C):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in matrix:
            replica = i.copy()
            j = len(i) - 1
            m = 0
            while j >= 0:
                i[j] = replica[m]
                j-=1
                m+=1
        return(matrix)
                
