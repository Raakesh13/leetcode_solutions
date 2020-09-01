#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.


def minimumMoves(n, grid, startX, startY, goalX, goalY):
    count = 0
    visited = []

    def pathCount(n, grid, startX, startY, goalX, goalY, count, visited):
        print(visited)
        if startX == goalX and startY == goalY:
            return count
        elif grid[startX][startY] == "X" or startX < 0 or startY < 0 or (grid[startX][startY]) in visited or startX > n or startY > n:
            return 0
        else:
            visited.append([startX, startY])
            count = count + 1
            # print(startX,startY)
            res = max(pathCount(n, grid, startX-1, startY, goalX, goalY, count, visited), pathCount(n, grid, startX+1, startY, goalX, goalY, count, visited),
                      pathCount(n, grid, startX, startY+1, goalX, goalY, count, visited), pathCount(n, grid, startX, startY-1, goalX, goalY, count, visited))
            return res
        # elif (startX == 0 and startY == 0):

    count = pathCount(n, grid, startX, startY, goalX, goalY, count, visited)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(n, grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
