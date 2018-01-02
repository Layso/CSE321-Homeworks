# This algorithm fills a cost table from given input land map. First fills first
# column with given values of money. Then on each step, starting from second
# column, cells sums their own money value with max possible stolen value from
# previous step. When all columns are done, last columns are filled with max
# amount of stolen money as last location of path. Returning biggest element of
# last column gives the answer.

# Algorithm does n*m iterations on each possible situation. If comparisons
# and assignments count as constant time work then it takes 3 + n + n*m*8 + n
# = 8nm + 2n + 3 = 8nm + 3n +3 = O(nm) time for worst case to find maximum
# amount of stolen money



def theft(land):
    height = len(land)
    width = len(land[0])
    costMap = [[None for i in range(width)] for j in range(height)]

    # Initializing first column with normal values
    for i in range(0, height):
        costMap[i][0] = land[i][0]

    # On each step filling up row with actual value of cell and max possible
    # stolen value from previous step. Repeat until all columns are filled
    for j in range(1, width):
        for i in range(0, height):
            col = j-1
            upIndex, midIndex, downIndex = i-1, i, i+1
            upValue, midValue, downValue = 0, 0, 0

            midValue = costMap[midIndex][col]
            if (upIndex >= 0):
                upValue = costMap[upIndex][col]
            if (downIndex < height):
                downValue = costMap[downIndex][col]

            costMap[i][j] = land[i][j] + max(upValue, midValue, downValue)

    # Finding max value to return
    maxValue = 0
    for i in range(0, len(costMap)):
        if costMap[i][height-1] > maxValue:
            maxValue = costMap[i][height-1]

    return maxValue



amountOfMoneyInLand= [[1,3,1,5],
                      [2,2,4,1],
                      [5,0,2,3],
                      [0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res)
# Expected Output: 16

amountOfMoneyInLand= [[10,33,13,15],
                      [22,21,4,1],
                      [5,0,2,3],
                      [0,6,14,2]]
res = theft(amountOfMoneyInLand)
print(res)
# Expected Output: 83
