def maxmin(arr,k):
    n=len(arr)
    arr.sort()
    print(k,"nd minimum element in given array is : ",arr[k-1])
    print(k,"nd maximum element in given array is : ",arr[n-k])
arr=[0,1,2,3,6,4,8,10]
maxmin(arr,2)
# 2 nd minimum element in given array is :  1
# 2 nd maximum element in given array is :  8




def merge_sort(arr):
    #divide
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        merge_sort(l)
        merge_sort(r)
    
    #conquer
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            elif r[j]<l[i]:
                arr[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1

def maxmin(arr,k):
    n=len(arr)
    merge_sort(arr)
    print(k,"nd minimum element in given array is : ",arr[k-1])
    print(k,"nd maximum element in given array is : ",arr[n-k])
arr=[0,1,2,3,6,4,8,10]
maxmin(arr,2)
# 2 nd minimum element in given array is :  1
# 2 nd maximum element in given array is :  8