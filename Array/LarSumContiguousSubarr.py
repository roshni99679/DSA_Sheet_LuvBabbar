'''Largest Sum Contiguous Subarray'''
#Kadanes Algorithm

def maxSumSubArr(arr):
    n=len(arr)
    max_sum=0
    current_sum=0
    for i in range(n):
        current_sum+=arr[i]
        #if at any point current_sum becomes greater than max_sum , set max_sum as current_sum         
        if current_sum>max_sum:     
            max_sum=current_sum
        #if at any point current_sum becomes 0, initialize current_sum from 0 again(leave current subarray and repeat same process from next subarray)
        if current_sum<0:                 
            current_sum=0
    return max_sum
arr=[5,-4,-2,6,-1]
print(maxSumSubArr(arr))
#6
#This code doesnt work if all elements are negative
'''Time Complexity : O(n)
Space Complexity : O(1)'''

#code that will run even if all ele are negative
def maxSubArraySum(arr,N):
        ##Your code here
        for i in range(1,N):
            if arr[i-1]>0:
                arr[i]+=arr[i-1]
        return max(arr)
arr=[5,-4,-2,6,-1]
print(maxSubArraySum(arr,len(arr)))
#6