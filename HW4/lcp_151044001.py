# This is just like the algorithm on part1 (see subarray_finder_151044001 for
# more information). On each step; divide array into two subarrays, do recursive
# call for each to get their longest common postfix (LCP). Then compare both
# LCPs came from subarrays to find their LCP. And return the result. Each step will
# take 2 * T(n/2) plus finding LCP time. Finding LCP would take constant time. So recurrence
# relation for this function would be T(n) = 2 * T(n/2) + 4  which is equivalent
# to O(log(n))



# Returns the common characters (from the end) in given strings
def find_common(s1, s2):
    s1Index = len(s1)-1
    s2Index = len(s2)-1
    common = 0

    # If one of the string is empty return None immediately
    if (s1Index < 0 or s2Index < 0):
        return None

    # Iterating characters from end to first mismatching index
    while (s1[s1Index-common] == s2[s2Index-common]) and (common<=min(s1Index, s2Index)):
        common += 1

    # Returning subarray from first mismatching index to end
    return s1[s1Index-common+1:]



# Finds longest common postfix of the strings in array
def longest_common_postfix(array):
    length = len(array)
    mid = int(length/2)

    # If array has one element, longest common postfix is itself
    if (length == 1):
        return array[0]

    else:
        # Else split array into two parts
        left = array[0:mid]
        right = array[mid:length]

        # Find both their longest common postfixes
        leftLCP = longest_common_postfix(left)
        rightLCP = longest_common_postfix(right)

        # Return common part of their postfixes
        return find_common(leftLCP, rightLCP)




inpStrings = ["absorptivity", "circularity", "electricity", "importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)
# Expected output: ity
print(lcp)
