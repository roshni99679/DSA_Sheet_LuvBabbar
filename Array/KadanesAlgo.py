def maxSubArray(nums):
    c_sum = 0
    max_sum = -1e8
    for i in range(len(nums)):
        c_sum += nums[i]
        if c_sum > max_sum:
            max_sum = c_sum
        if c_sum < 0:
            c_sum = 0
    return max_sum

def maxsumsubarr(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] > 0:
            arr[i] += arr[i-1]
            # print(arr[i],end=" ")     #1 -1 5
    # print(arr)  #[5, 1, -1, 6, 5]
    return max(arr)


arr = [5, -4, -2, 6, -1]
print(maxsumsubarr(arr))
# 6

