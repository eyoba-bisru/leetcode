from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0:
            return []

        output = []

        output.extend(matrix.pop(0))

        for i in range(len(matrix) - 1):
            if matrix[i]:
                output.append(matrix[i].pop())

        if len(matrix) != 0 and matrix[-1]:
            output.extend(matrix.pop()[::-1])

        for j in range(len(matrix) - 1, -1, -1):
            if matrix[j]:
                output.append(matrix[j].pop(0))

        output.extend(self.spiralOrder(matrix))
        return output
