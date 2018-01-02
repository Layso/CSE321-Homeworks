def compareScales (leftScaleList, rightScaleList):
    # Left and right scale lists must be at same length to have an accurate
    # result. Otherwise it may cause errors when scales are actually equal
	# We assume this function takes constant time
    result = sum(leftScaleList) - sum(rightScaleList)
    if (result < 0):
        return 1
    elif (result > 0):
        return -1
    else:
        return 0



# The summary of the algorithm is splitting array into 2 sub arrays
# to search rotten walnut in the lighter sub array, just like binary
# search. Basically doing log(2 base n) operations in average which
# also equals to worst case. Best case that could happen to find a
# rotten walnut is when the rotten walnut is on middle of the array
# So best case takes omega(logn) time. This also equals to scenario
# when there is no rotten walnut
def findRotten(walnuts):
	# Constant time operations
	length = len(walnuts)
	midIndex = int(length/2)


	# Base case is when given array has only one element
	# If only walnut is rotten, return 0 (index)
	# Constant time operations
	if length == 1:
		if (walnuts[0] == 0.5):
			return 0

		else:
			return -1

	# Splitting walnut array to 2 sub-arrays to keep searching
	# Constant time operations
	left = walnuts[0:midIndex]
	right = walnuts[midIndex:length]

	# Controlling even numbered array
	if not length%2:
		# Continue search with lighter sub-array, return coming index
		# plus current index of walnut
		# It takes theta(T(n/2)) time to calculate further operations
		result = compareScales(left, right)
		if result == 1:
			return findRotten(left)

		elif result == -1:
			return findRotten(right) + midIndex

		else:
			return -1

	# Controlling odd numbered array
	else:
		# If middle element is rotten, return midIndex
		mid = right.pop(0)
		if mid == 0.5:
			return midIndex

		# Continue search with lighter sub-array, return coming index
		# plus current index of walnut
		# It takes theta(T(n/2)) time to calculate further operations
		result = compareScales(left, right)
		if result == 1:
			return findRotten(left)

		elif result == -1:
			return findRotten(right) + midIndex + 1

		else:
			return -1




arr = [1, 1, 1, 1, 1, 0.5, 1]
print("The index of rotten walnut is: " + str(findRotten(arr)))
