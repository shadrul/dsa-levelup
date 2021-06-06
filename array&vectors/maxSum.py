# maximum subarray continuous sum
import sys
def maxSum(nums):
    if(len(nums)<2):
        return nums[0]
    g = nums[0]
    local = nums[0]
    for i in range(1,len(nums)):
        local = max(nums[i],local+nums[i])
        g = max(g,local)
    return g
        
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    result = maxSum(arr)
    print(result)
    