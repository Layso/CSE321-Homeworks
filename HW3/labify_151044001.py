


def findMinimumCostToLabifyGTU(labCost, roadCost, mapping):
	if (labCost < roadCost):
		return len(mapping)*labCost

	else:
		labCount = 0
		roadCount = 0

		return labCount*labCost + roadCount*roadCount




mapOfGTU = {
	1 : set([2,3]),
	2 : set([1,3,4]),
	3 : set([1,2,4]),
	4 : set([3,2]),
	5 : set([6]),
	6 : set([5]) } # graph is initialized as dictionary


minCost = findMinimumCostToLabifyGTU(5,2,mapOfGTU)
print(minCost)# Output will be 18
