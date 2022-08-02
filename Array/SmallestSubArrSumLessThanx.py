'''Smallest subarray with sum greater than a given value
Given an array of integers and a number x, find the smallest subarray with sum greater than the given value. 

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.'''



# Python3 program to find Smallest
# subarray with sum greater
# than a given value

# Returns length of smallest subarray
# with sum greater than x. If there
# is no subarray with given sum,
# then returns n+1
def smallestSubWithSum(arr, n, x):

	# Initialize length of smallest
	# subarray as n+1
	min_len = n + 1

	# Pick every element as starting point
	for start in range(0,n):
	
		# Initialize sum starting
		# with current start
		curr_sum = arr[start]

		# If first element itself is greater
		if (curr_sum > x):
			return 1

		# Try different ending points
		# for curremt start
		for end in range(start+1,n):
		
			# add last element to current sum
			curr_sum += arr[end]

			# If sum becomes more than x
			# and length of this subarray
			# is smaller than current smallest
			# length, update the smallest
			# length (or result)
			if curr_sum > x and (end - start + 1) < min_len:
				min_len = (end - start + 1)
		
	return min_len
arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x)
if res1 == n1+1:
	print("Not possible")
else:
	print(res1)

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x)
if res2 == n2+1:
	print("Not possible")
else:
	print(res2)

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
if res3 == n3+1:
	print("Not possible")
else:
	print(res3)
#3
#1
#4

'''Time Complexity: O(n).
Auxiliary Space: O(1)'''

def small(arr,x):
	minLen=len(arr)+1
	for start in range(0,len(arr)):
		currSum=arr[start]
		if currSum>x:
			return 1
		for end in range(start+1,len(arr)):
			currSum+=arr[end]
			if currSum>x and end-start+1<minLen:
				minLen=end-start+1
	return minLen
arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]

x = 280
res3 = small(arr3, x)
if res3 == n3+1:
	print("Not possible")
else:
	print(res3)
