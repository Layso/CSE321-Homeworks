# The difference between lomuto and hoare partitioning is; hoare saerches
# the subarray from both sides with two indicators while on lomuto there is one
# indicator that shift while the other is still. In my opinion hoare is more
# simple to understand and implement easily. At least that was my thought after
# I first hear them on class. Both implementations are easy but still Hoare's
# algorithm is (for me) more convincing that it partitions a subarray with a
# random pivot. Also from the scientific approach according to my research;
# hoare will never do swap on a subarray that is already sorted, while lomuto
# does n/2 swaps. All same element arrays are another case. Hoare does swap
# but finds pivot in middle but lomuto have its worst case so it degrades the
# performance to Θ(n^2). As I understand here using hoare has more advantages
# than lomuto. I tried to implement pseudeucode on our notebooks but somehow
# failed due to an infinite loop issue. I found a solution and rearrenged the
# implementation according to it by swapping smaller indicator and larger
# indicator shifts. See commented area above fn hoare for more clear description

# References
# https://cs.stackexchange.com/questions/11458/quicksort-partitioning-hoare-vs-lomuto
# https://kluedo.ub.uni-kl.de/frontdoor/index/index/docId/3463
# https://stackoverflow.com/questions/12520555/hoare-partitioning-falls-into-infinite-loop



# Function to partition array A[l..r] with Nico Lomuto's algorithm
def lomuto(A, l, r):
	p = A[l]	# Taking first element as pivot
	s = (l)		# Represents the last index of smaller elements

	# This loop gathers elements smaller than pivot to right and others to left
	for i in range(l+1, r+1):
		# If current element is smaller than pivot, swap current with smaller
		# element and increase index of smaller element
		if (A[i] < p):
			s = s+1
			A[s], A[i] = A[i], A[s]

	# Taking pivot to its position
	A[s], A[l] = A[l], A[s]
	return s



'''
# Function to partition array A[l..r] with Tony Hoare's algorithm
def hoare(A, l, r):
	p = A[l]	# Taking first element as pivot
	i = l		# Indicator for smaller elements
	j = r+1		# Indicator for bigger elements


	# On each step shift indicators to middle until they both find a misplaced
	# element, swap both elements, return until indicators meet.
	while True:
		# Shift smaller indicator to find larger element
		while True:
			i += 1
			if (A[i] >= p):
				break

		# Shift larger indicator to find smaller element
		while True:
			j -= 1
			if (A[j] <= p):
				break

		# If indicators, meet return pivot's position
		if (i >= j):
			return j

		# Swap the misplaced elements
		A[i], A[j] = A[j], A[i]
'''
# Function to partition array A[l..r] with Tony Hoare's algorithm
def hoare(A, l, r):
	p = A[l]	# Taking first element as pivot
	i = l-1		# Indicator for smaller elements
	j = r+1		# Indicator for bigger elements

	# On each step shift indicators to middle until they both find a misplaced
	# element, swap both elements, return until indicators meet.
	while True:
		# Shift larger indicator to find smaller element
		while True:
			j -= 1
			if A[j] <= p:
				break

		# Shift smaller indicator to find larger element
		while True:
			i += 1
			if A[i] >= p:
				break

		# If indicators meet return pivot's position, else swap the misplaced elements
		if (i >= j):
			return j

		A[i], A[j] = A[j], A[i]



# Quicksort helper function for recursion
def quickSortHelper(array, low, high, partition):
	# If array has 1 or 0 elements, no need of work
	if (high > low):
		# Partitioning the array
		if (partition):
			position = lomuto(array, low, high)
		else:
			position = hoare(array, low, high)


		# Sorting
		quickSortHelper(array, low, position, partition)
		quickSortHelper(array, position+1, high, partition)
		return array



# Given signature of quicksort with hoare partition
def quickSortHoare(array):
	# Starts recursion with 0, indicates hoare partition
	return quickSortHelper(array, 0, len(array)-1, 0)



# Given signature of quicksort with lomuto partition
def quickSortLomuto(array):
	# Starts recursion with 1, indicates lomuto partition
	return quickSortHelper(array, 0, len(array)-1, 1)



arr1 = [24, 4, 68, 17, 75, 16, 42]
arr2 = [24, 4, 68, 17, 75, 16, 42]

qsh = quickSortHoare(arr1)
# Expected output: [4, 15, 16, 24, 42, 68, 75]
print(qsh)

qsl = quickSortLomuto(arr2)
# Expected output: [4, 15, 16, 24, 42, 68, 75]
print(qsl)
