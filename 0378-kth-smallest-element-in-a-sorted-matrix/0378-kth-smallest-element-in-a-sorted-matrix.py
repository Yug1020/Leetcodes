import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                lst.append(matrix[i][j])
        
        heapq.heapify(lst)

        for i in range(k - 1):
            heapq.heappop(lst)
        
        return heapq.heappop(lst)