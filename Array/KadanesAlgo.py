def maxSubArraySum(arr,N):
        ##Your code here
        for i in range(1,N):
            if arr[i-1]>0:
                arr[i]+=arr[i-1]
        return max(arr)
arr=[5,-4,-2,6,-1]
print(maxSubArraySum(arr,len(arr)))
#6
#Runs even if all ele are negative 

def maxsumsubarr(arr):
    n=len(arr)
    for i in range(1,n):
        if arr[i-1]>0:
            arr[i]+=arr[i-1]
            # print(arr[i],end=" ")     #1 -1 5
    # print(arr)  #[5, 1, -1, 6, 5]
    return max(arr)
arr=[5,-4,-2,6,-1]
print(maxsumsubarr(arr))
#6

