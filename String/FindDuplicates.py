
def findDuplicates(nums):
        n=len(nums)
        count={}
        arr=[]*n
        count = {}
        for i in range(n):
            if(nums[i] in count):
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for k,v in count.items():
            if v>1:
                arr.append(k)
        return arr
print(findDuplicates([4,3,2,7,8,2,3,1]))
#[3, 2]
'''Time Complexity: O(N), where N = length of the string passed and it takes O(1) time to insert and access any element in an unordered map
Auxiliary Space: O(K), where K = size of the map (0<=K<=input_string_length).'''