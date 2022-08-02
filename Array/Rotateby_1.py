'''Program to cyclically rotate an array by one'''

def rotate(arr):
    n=len(arr)
    last=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last
arr=[1,2,3,4,5,6]
rotate(arr)
print(arr)
#[6, 1, 2, 3, 4, 5]

def rotate(arr):
    n=len(arr)
    last_ele=arr[n-1]
    i=n-1
    while i>=0:
        arr[i]=arr[i-1]
        i-=1
    arr[0]=last_ele
arr=[1,2,3,4,5,6]
rotate(arr)
print(arr)
#[6, 1, 2, 3, 4, 5]

'''Time Complexity: O(n) As we need to iterate through all the elements 
Auxiliary Space: O(1)'''