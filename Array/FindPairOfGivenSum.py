'''Count pairs with given sum
EasyAccuracy: 41.59%Submissions: 100k+Points: 2
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, K = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function getPairsCount() which takes arr[], n and k as input parameters and returns the number of pairs that have sum K.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
1 <= K <= 108
1 <= Arr[i] <= 106

 '''


def countPair(arr,sum):
    n=len(arr)
    count=0
    hm={}
    for i in range(n):
        if sum-arr[i] in hm:
            count+=hm[sum-arr[i]]
        if arr[i] in hm:
            hm[arr[i]]+=1
        else:
            hm[arr[i]]=1

    return count
arr=[1,1,1,1]
print(countPair(arr,2))
#6
'''Time Complexity: O(n), to iterate over the array
Auxiliary Space: O(n), to make a map of size n'''
