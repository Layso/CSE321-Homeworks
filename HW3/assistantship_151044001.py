# List to store permutations
permutationList = []

# Other department work time
otherWork = 6

# Free R.A. indicator
freeAssistant = -1



# List printer function to organize test display
def printList(array):
	for i in range(0, len(array)):
		print(array[i])



# Heap's algorithm as suggested on moodle
def permutation(array, step):
    if (step == 1):
        permutationList.append(list(array))

    for i in range(0, step):
        permutation(array, step-1)

        if step % 2 == 1:
            temp = array[0]
            array[0] = array[step-1]
            array[step-1] = temp

        else:
            temp = array[i];
            array[i] = array[step-1];
            array[step-1] = temp;



# Function to solve assignment problem
def findOptimalAssistantship(table):
	resultArray = []
	resultHours = float("inf")
	assistantCount = len(table)
	courseCount = len(table[0])


	for i in range(0, courseCount):
		resultArray.append(i)

	if assistantCount > courseCount:
		for i in range(0, assistantCount-courseCount):
			resultArray.append(freeAssistant)

	permutation(resultArray, len(resultArray))

	for i in range(0, len(permutationList)):
		tempResultArray = permutationList[i]
		tempresultHours = 0

		for j in range(0, len(tempResultArray)):
			k = tempResultArray[j]

			if k == freeAssistant:
				tempresultHours += otherWork
			else:
				tempresultHours += table[j][k]

		if tempresultHours < resultHours:
			resultHours = tempresultHours
			resultArray = tempResultArray

	return resultArray, resultHours



table = [   [5,8,7,4],  #RA 0
            [8,12,7,4], #RA 1
            [4,8,5,4],  #RA 2
            [1,2,3,4]]  #RA 3


    # Courses  0  1   2
inputTable = [[1, 8,  7],  # R.A. 0
			  [8, 12, 7],  # R.A. 1
			  [9, 5, 8],  # R.A. 2
			  [10, 5, 2],  # R.A. 3
			  [4, 8,  5]]  # R.A. 4

arr, hr = findOptimalAssistantship(table)
print(arr)
print(hr)
