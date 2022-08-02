'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?'''



'''
elements count: N
len of arr : N+1 
let N=5
len(arr)=6
number of ele : 5 in range(0 to 5)
so arr will have atleast one duplicate ele to fill arr to its len
ex: [1,2,3,4,5,2]
'''
#abs(-2)=2.....abs() converts negative numbers to positive

def findDups(arr):
    n=len(arr)
    for i in range(n):
        index=abs(arr[i])               #index=1
        if arr[index]<0:return index    #arr[index]=2(2>0) (arr[index]>0 : implies arr[i]=index=1 is not yet visited)
        arr[index]= - arr[index]        #arr[index]=-2 (if arr[index]<0 : implies arr[i]=index=1 is visited)
    return -1
arr=[1,2,2,3,4,5]  
print(findDups(arr))
#2
'''Time complexity : O(n)
Space Complexity : O(1)'''



