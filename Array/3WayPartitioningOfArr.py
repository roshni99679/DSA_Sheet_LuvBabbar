'''Three way partitioning of array

Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.


Example 1:

Input: 
n = 5
A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 1
Explanation: One possible arrangement is:
{1, 2, 3, 3, 4}. If you return a valid
arrangement, output will be 1.


Example 2:

Input: 
n = 3 
A[] = {1, 2, 3}
[a, b] = [1, 3]
Output: 1
Explanation: One possible arrangement 
is: {1, 2, 3}. If you return a valid
arrangement, output will be 1.


Your Task:
You dont need to read input or print anything. The task is to complete the function threeWayPartition() which takes the array[], a and b as input parameters and modifies the array in-place according to the given conditions.
Note: The generated output is 1 if you modify the given array successfully.


Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
'''

'''Three way partitioning of an array around a given range


Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts. 

All elements smaller than lowVal come first. 
All elements in range lowVal to highVal come next. 
All elements greater than highVal appear in the end. 
The individual elements of three sets can appear in any order.

Examples: 

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
        lowVal = 14, highVal = 20
Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
       lowVal = 20, highVal = 20       
Output: arr[] = {1, 14, 5, 4, 2, 1, 3, 20, 20, 98, 87, 32, 54} 



A simple solution is to sort the array. This solution does a lot of extra rearrangements and requires O(n Log n) time.

An efficient solution is based on Dutch National Flag based QuickSort. We traverse given array elements from left. We keep track of two pointers, first (called start in the code below) to store next position of smaller element (smaller than range) from beginning; and second (called end in the code below) to store next position of greater element from end. 
'''


def part(arr,low,high):
    n=len(arr)
    # Initialize next available positions for smaller (than range) and greater elements
    start=0
    end=n-1
    i=0
    # Traverse elements from left
    while i<=end:
        # If current element is smaller than range, put it on next available smaller position.
        if arr[i]<low:
            arr[i],arr[start]=arr[start],arr[i]
            start+=1
            i+=1
        # If current element is greater than range, put it on next available greater position.
        elif arr[i]>high:
            arr[i],arr[end]=arr[end],arr[i]
            end-=1
        else:
            i+=1
arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
part(arr,10,20)
print(arr)
#[1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54]
'''Time Complexity: O(n) 
Auxiliary Space: O(1)'''