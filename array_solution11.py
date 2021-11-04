class Solution:
    def rotateImage(matrix: list[list[int]]): #rotating 90 degrees clockwise
        matrix[:] = map(list, zip(*reversed(matrix)) )
        return matrix

print(Solution.rotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))