

def reverseArray(arr):
    n=len(arr)
    start=0
    end=n-1
    while start<=end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=[1,2,3,4,5,5,6]
reverseArray(arr)
print(arr)
#[6, 5, 5, 4, 3, 2, 1]



def reverse(arr):
    n=len(arr)
    start=0
    end=n-1
    while start<=end:
        arr[start]=temp
        temp=arr[end]
        arr[end]=arr[start]
        start+=1
        end-=1
arr=[1,2,3,4,5,5,6]
reverseArray(arr)
print(arr)
#[6, 5, 5, 4, 3, 2, 1]




def reverseArray(arr,start,end):
    if start>=end:
        return
    arr[start],arr[end]=arr[end],arr[start]
    reverseArray(arr,start+1,end-1)
arr=[1,2,3,4,5,5,6]
reverseArray(arr,0,len(arr)-1)
print(arr)
#[6, 5, 5, 4, 3, 2, 1]
