'''Minimum swaps required to bring all elements less than or equal to k together

Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the numbers less than or equal to k together. 
 

Input:  arr[] = {2, 1, 5, 6, 3}, k = 3
Output: 1

Explanation: 
To bring elements 2, 1, 3 together, swap 
element '5' with '3' such that final array
will be-
arr[] = {2, 1, 3, 6, 5}

Input:  arr[] = {2, 7, 9, 5, 8, 7, 4}, k = 5
Output: 2'''

def minswaps(arr,k):
    n=len(arr)
    badele=0
    count=0
    for i in range(n):
        if arr[i]>k:
            badele+=1
        elif badele>0:
            tmp=arr[i]
            arr[i]=arr[i-badele]
            arr[i-badele]=tmp
            count+=1
    return count
arr=[2, 7, 9, 5, 8, 7, 4]
k=5
print(minswaps(arr,k))
#5


def minSwaps(arr,k):
    swaps=0
    badele=0
    for i in range(len(arr)):
        #we will increment our badele only if we see an element greater than K
        if arr[i]>k:
            badele+=1
        #this case will handle if we see an element less than <= k,then we will swap the element arr[i] which is less than K, with our first element of badele window which is greater than K
        elif badele>0:
            arr[i],arr[i-badele]=arr[i-badele],arr[i]
            swaps+=1
    return swaps
arr=[2, 7, 9, 5, 8, 7, 4]
k=5
print(minSwaps(arr,k))
#2