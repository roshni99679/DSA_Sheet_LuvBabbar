'''Find if there is a subarray with 0 sum

Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.'''

def subarr0(arr):
    n=len(arr)
    count=0
    sum=0
    hm={}
    for i in range(n):
        if sum-arr[i] in hm:
            count+=hm[sum-arr[i]]
            return True

        if arr[i] in hm:
            hm[arr[i]]+=1
        else:
            hm[arr[i]]=1
    return False
ans=subarr0([1,81,-2,9,-2])
if (ans):
    print("Found")
else:
    print("Not found")
#Not Found
'''Time Complexity of this solution can be considered as O(n) under the assumption that we have good hashing function that allows insertion and retrieval operations in O(1) time. 
Space Complexity: O(n) .Here we required extra space for unordered_set to insert array elements.'''


def subArr(arr,sum):
    n=len(arr)
    count=0
    hm={}
    for i in range(n):
        if sum-arr[i] in hm:
            count+=hm[sum-arr[i]]
            return True
        if arr[i] in hm:
            hm[arr[i]]+=1
        else:
            hm[arr[i]]=1
    return False
arr=[1,2,-1,3,4,5,-5]
ans=subArr(arr,0)
if (ans):
    print("Found")
else:
    print("Not found")
#Found
