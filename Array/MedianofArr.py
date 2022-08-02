def median(arr):
    n=len(arr)
    if n==2:
        return (arr[0]+arr[1])//2
    if n%2 !=0:
        return arr[n//2]
    else:
        return (arr[int((n-1)/2)]+arr[int(n/2)])//2
arr=[1,2,4,5]
print(median(arr))
#3