# This algorithm is basically splitting array into 2 parts until it becomes all
# 1 elemented subarrays. Each step gets the subarray of minimum sum from left
# and right subarrays. Also another subarray that is minimum sum subarray of
# whole list, searching from middle expanding to sides. Searching middle to sides
# takes linear time, since it starts from mid index and goes to start & end seperately
# whole array will be searched. Recursive calls are T(n/2), since we do recursive
# call for each half it is 2 * T(n/2). Remaining operations (assignments, arithmetic
# operations, finding max, etc.) would take no longer than linear time. So recurrence
# relation for function min_subarray_finder would be T(n) = 2T(n/2) + n. Using Master's
# theorem the worst case would be O(n * log(n))



# Starting from middle, searches expanding to the right & left to find 2 indexes.
# Subarray between this 2 indexes indicates the subarray that have minimum sum
def min_middle_subarray_finder(array):
	# Preparing variables
	length = len(array)
	mid = int(length/2)
	leftMostIndex = mid
	rightMostIndex = mid


	# Starting search from mid to left
	index = mid
	sum = 0
	tempSum = sum
	while(index>=0):
		tempSum += array[index]
		if (tempSum<sum):
			sum = tempSum
			leftMostIndex = index
		index -= 1

	# Starting search from right to mid
	index = mid+1
	sum = 0
	tempSum = sum
	while(index<=length-1):
		tempSum += array[index]
		if (tempSum<sum):
			sum = tempSum
			rightMostIndex = index
		index += 1

	# Returning part of array that gives minimum sum
	return array[leftMostIndex:rightMostIndex+1]



# Main function, splits array into 2 sub arrays, does recursive call on
# subarrays and calls a search function to get another subarray that search
# minimum sum from middle to right & left. Compares all 3 subarrays and returns
# the one that have minimum sum
def min_subarray_finder(array):
	length = len(array)

	# If array has 1 element then minimum subarray is itself
	if (length == 1):
		return array

	else:
		# Else split array into 2 parts and search for minimum subarrays on them
		# Also search minimum sum subarray in whole array starting search from middle
		mid = int(length/2)
		midArray = min_middle_subarray_finder(array)
		leftArray = min_subarray_finder(array[0:mid])
		rightArray = min_subarray_finder(array[mid:length])

		# Get sum of each found array
		midArrayMin = sum(midArray)
		leftArrayMin = sum(leftArray)
		rightArrayMin = sum(rightArray)
		minimum = min(leftArrayMin, midArrayMin, rightArrayMin)

		# Return the array that has minimum sum
		if (minimum == leftArrayMin):
			return leftArray
		elif (minimum == rightArrayMin):
			return rightArray
		else:
			return midArray











inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
#inpArr = [-2, -4, 5,-5, 1, -3]
msa = min_subarray_finder(inpArr)
msa = min_middle_subarray_finder(inpArr)
# Expected output: [-4, -7, 5, -13]
print(msa)
# Expected output: -19
print(sum(msa))
