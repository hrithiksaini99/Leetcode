class Solution:
    def firstCompleteIndex(self, arr, mat):
        index_map = {num: i for i, num in enumerate(arr)}
        n, m = len(mat), len(mat[0])
        result = float('inf')

        # Check rows
        for row in mat:
            max_index = max(index_map[num] for num in row)
            result = min(result, max_index)

        # Check columns
        for col in zip(*mat): # zip(*mat): is used to take transpose of the matrix
            max_index = max(index_map[num] for num in col)
            result = min(result, max_index)

        return result