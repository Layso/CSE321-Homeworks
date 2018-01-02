# Algorithm is pretty simple. Second list that derived from the first one
# will have elements equal to original or 1 to get the maximum cost. So on each
# step it will check if it is better to take 1 or number's original value
# Second list has 2 fields to store these possibilities. Repeates until all
# elements on original list are done. Finally the maximum value of last element
# on second list will represent the maximum cost of second list (X in PDF)

# Algorithm has only 1 loop that iterates n-1 times (where n is length of the
# input list, Y) has 2 simple assignments inside and 2 extra assignments on the
# beginning. The sum will be 2*n + 2 and also a linear search to check if all
# elements are bigger than 1 takes plus n = 3n + 2 = O(n) time for worst case



def listChecker(list):
    for i in range(0, len(list)):
        print(list[i])
        if list[i] < 1:
            return -1
    else:
        return 1


def find_maximum_cost(originList):
    length = len(originList)
    secondList = [[0 for i in range(2)] for j in range(length)]

    # Checking if all elements are bigger than zero
    if (listChecker(originList) == -1):
        return -1

    # Looking for best possibilitiy of each element to take it as 1 or it's
    # original value
    for i in range (1,length):
        first = secondList[i-1][0]                                          # Value of total, assumed previous as 1
        second = secondList[i-1][1] + originList[i-1]-1                     # Assuming current element as 1
        third = secondList[i-1][0] + originList[i]-1                        # Assuming previous element as 1
        fourth = secondList[i-1][1] + abs(originList[i] - originList[i-1])  # Real interval between current and previous elements

        # Finding best possible values
        secondList[i][0] = max(first, second)
        secondList[i][1] = max(third, fourth)

    return max(secondList[length-1])





Y = [14,1,14,1,14]
cost = find_maximum_cost(Y)
print(cost)
# Expected Output: 52

Y = [1,9,11,7,3]
cost = find_maximum_cost(Y)
print(cost)
# Expected Output: 28

Y = [50,28,1,-1,13,7]
cost = find_maximum_cost(Y)
print(cost)
# Expected Output: 78
