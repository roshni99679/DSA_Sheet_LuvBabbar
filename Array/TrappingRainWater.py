
class Solution:
    def trappingWater(self, arr,n):
        left,right = 0,(n-1)
        res = 0
        maxleft,maxright = 0,0
        
        while(left <= right):
            if(arr[left] <= arr[right]):
                if(arr[left] >= maxleft):
                    maxleft = arr[left]
                else:
                    res += maxleft - arr[left]
                left += 1
            else:
                if(arr[right] >= maxright):
                    maxright = arr[right]
                else:
                    res += maxright - arr[right]
                right -= 1
                
        return res
arr=[8 ,8 ,2 ,4 ,5 ,5 ,1]
obj=Solution()
print(obj.trappingWater(arr,len(arr)))
#4


'''Time complexity: O(n). Single iteration of O(n)O(n).
Space complexity: O(1) extra space. Only constant space required for \text{left}left, \text{right}right, \text{left\_max}left_max and \text{right\_max}right_max.'''






