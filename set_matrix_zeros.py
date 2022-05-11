class Solution:
    def setZeroes_v1(self, matrix):  # O(n+m) space complexity
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows = [False] * len(matrix)
        cols = [False] * len(matrix[0])
        for r in range(len(rows)):
            for c in range(len(cols)):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(len(rows)):
            if rows[r]:
                for c in range(len(cols)):
                    matrix[r][c] = 0
        for c in range(len(cols)):
            if cols[c]:
                for r in range(len(rows)):
                    matrix[r][c] = 0

    def setZeroes(self, matrix): # O(1) memory cols is matrix[0], rows[1:] is matrix[1:][0], need a flag for rows[0]
        n = len(matrix)
        m = len(matrix[0])
        firstRow = False
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstRow = True
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(n):
                matrix[r][0] = 0
        if firstRow:
            for c in range(m):
                matrix[0][c] = 0








if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)
