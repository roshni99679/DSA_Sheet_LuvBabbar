'''Given heights of n towers and a value k. We need to either increase or decrease the height of every tower by k (only once) where k > 0. The task is to minimize the difference between the heights of the longest and the shortest tower after modifications and output this difference.

Examples: 

Input  : arr[] = {1, 15, 10}, k = 6
Output :  Maximum difference is 5.
Explanation : We change 1 to 7, 15 to 9 and 10 to 4. Maximum difference is 5 (between 4 and 9). We can't get a lower difference.

Input : arr[] = {1, 5, 15, 10} 
          k = 3   
Output : Maximum difference is 8 arr[] = {4, 8, 12, 7}

Input : arr[] = {4, 6} 
         k = 10
Output : Maximum difference is 2 arr[] = {14, 16} OR {-6, -4}

Input : arr[] = {6, 10} 
        k = 3
Output : Maximum difference is 2 arr[] = {9, 7} 

Input : arr[] = {1, 10, 14, 14, 14, 15}
        k = 6 
Output: Maximum difference is 5 arr[] = {7, 4, 8, 8, 8, 9} 

Input : arr[] = {1, 2, 3}
        k = 2 
Output: Maximum difference is 2 arr[] = {3, 4, 5} 


First, we try to sort the array and make each height of the tower maximum. We do this by decreasing the height of all the towers towards the right by k and increasing all the height of the towers towards the left (by k). It is also possible that the tower you are trying to increase the height doesn't have the maximum height. Therefore we only need to check whether it has the maximum height or not by comparing it with the last element on the right side which is a[n]-k. Since the array is sorted if the tower's height is greater than the [n]-k then it's the tallest tower available. Similar reasoning can also be applied to finding the shortest tower.  


Note:- We need not consider where a[i]<k because the height of the tower can't be negative so we have to neglect that case.
'''

#youtube explanation: https://www.youtube.com/watch?v=t8_uxrjqC2g

def min_maxdiff(arr,k,n):
    arr.sort()
    smallest=arr[0]     #in a sorted arr, smallest ele is the ele at 0 index
    largest=arr[n-1]    #in a sorted arr, largest ele is the ele at len(arr)-1 index
    diff=largest-smallest       #let current diff be largest - smallest
    for i in range(1,n):            #range(1,n) -> 0 to n-1
        if arr[i]-k<0:continue          #if negative dont do anything , leave
        smallest=min(arr[0]+k,arr[i]-k)     #find min of arr[0]+k and remaining ele(ele at index 1 to n-1)-k
        largest=max(arr[n-1]-k,arr[i-1]+k)      #find max of arr[n-1]-k and remaining ele(ele at index 0 to n-2)+k
        diff=min(diff,largest-smallest)             #find min of curr diff and prev diff
    return diff
arr=[7, 4, 8, 8, 8, 9]
k=6
n=len(arr)
print(min_maxdiff(arr,k,n))
#5
'''Time Complexity: O(nlogn)
Auxiliary Space: O(n)
'''


