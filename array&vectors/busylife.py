#Busy Life solution in nlogn
import sys

def compare(a,b):
    if(a[1] == b[1]):
        x = a[1] - a[0]
        y = b[1] -b[0]
        return x<y
    return a[1]<b[1]
    
    
def busyLife(nums):
    nums.sort(key = lambda n: (n[1],n[1]-n[0])) #sorts on the basis of finishing time and time difference
    x = 0
    count =0
    for i in range(len(nums)):
        if(nums[i][0]>=x):
            x = nums[i][1]
            count+=1
    return count
    
if __name__ == "__main__":
    n = int(input())
    arr =[]
    for i in range(n):
        x = tuple(map(int,input().split()))
        arr.append(x)
    result = busyLife(arr)
    print(result)