# Subarray sort 
import sys
def subSort(nums):
    l = -sys.maxsize - 1
    s = sys.maxsize
    n = len(nums)
    if(n<2):
        return 0
    if(nums[0]>nums[1]):
        l = max(l,nums[0])
        s = min(s,nums[0])
    for i in range(1,n-1):
        if(nums[i]>nums[i+1] or nums[i]<nums[i-1]):
            l = max(l,nums[i])
            s = min(s,nums[i])
    
    if(nums[n-1]<nums[n-2]):
        l = max(l,nums[n-1])
        s = min(s,nums[n-1])
    if(l==-sys.maxsize-1 and s==sys.maxsize):
        return 0
    j =0
    for i in range(n):
        if(nums[i]>s):
            j = i
            break
    
    x = 0 
    for k in range(n-1,-1,-1):
           if(nums[k]<l):
                x = k
                break
    return (x-j +1)


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    result = subSort(arr)
    print(result)
    