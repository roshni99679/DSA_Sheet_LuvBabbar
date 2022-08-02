'''Merge Without Extra Space

Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order without using any extra space.


Example 1:

Input:
N = 4, M = 5
arr1[] = {1, 3, 5, 7}
arr2[] = {0, 2, 6, 8, 9}
Output: 0 1 2 3 5 6 7 8 9
Explanation: Since you can't use any 
extra space, modify the given arrays
to form 
arr1[] = {0, 1, 2, 3}
arr2[] = {5, 6, 7, 8, 9}

Example 2:

Input:
N = 2, M = 3
arr1[] = {10, 12}
arr2[] = {5, 18, 20}
Output: 5 10 12 18 20
Explanation: Since you can't use any
extra space, modify the given arrays
to form 
arr1[] = {5, 10}
arr2[] = {12, 18, 20}
 

Your Task:
You don't need to read input or print anything. Complete the function merge() which takes the two arrays arr1[], arr2[] and their sizes n and m, as input parameters. The function does not return anything. Use the given arrays to sort and merge arr1[] and arr2[] in-place. 
Note: The generated output will print all the elements of arr1[] followed by all the elements of arr2[].


Expected Time Complexity: O((n+m)*log(n+m))
Expected Auxiliary Space: O(1)


Constraints:
1 <= N, M <= 5*104
0 <= arr1i, arr2i <= 106

 '''

#youtube link: https://www.youtube.com/watch?v=mF3ofENSeg8&list=PLzffTJx5aHaRMfFodb4O5yyi6uSA4Q3E0&index=12

def fixArray(arr2):
    #first element will always create problem in sorting bcoz of swapping of ele with arr1 therefore perform fixing(sorting) everytime after swap
    for i in range(1,len(arr2)):
        if arr2[i]<arr2[i-1]:
            arr2[i],arr2[i-1]=arr2[i-1],arr2[i]

def merge_sortedArr(a1,a2):
    l1=len(a1)
    l2=len(a2)
    i=j=0
    while i<l1:
        if a1[i]>a2[j]:
            a1[i],a2[j]=a2[j],a1[i]
            fixArray(a2)
        i+=1
        
 
a1=[0,1,4,7]
a2=[2,3,5,6,8]
merge_sortedArr(a1,a2)
print(a1,a2)
# [0, 1, 2, 3] [4, 5, 6, 7, 8]
'''TC: O(l1*l2)
SC: O(1)'''


def merge(a,b):
    n=len(a)
    m=len(b)
    c=[None]*(n+m)
    i=j=k=0
    while i<n and j<m:
        if a[i]<b[j]:
            c[k]=a[i]
            i+=1
        else:
            c[k]=b[j]
            j+=1
        k+=1

    while i<n:
        c[k]=a[i]
        i+=1
        k+=1
    while j<m:
        c[k]=b[j]
        j+=1
        k+=1
    return c
a=[0,1,4,7]
b=[2,3,5,6,8]
print(merge(a,b))
#[0, 1, 2, 3, 4, 5, 6, 7, 8]
'''Time Complexity : O(n1 + n2) 
Auxiliary Space : O(n1 + n2)'''
