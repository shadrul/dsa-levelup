# Triplets 

def triplets(nums,target):
    target = 0
    nums.sort()
    n = len(nums)
    result =[]
    for i in range(n-2):
        s = i+1
        e = n-1
        while(s<e):
            current_sum = nums[i]
            current_sum+=nums[s]
            current_sum+=nums[e]
            
            if(current_sum == target):
                x = [nums[i],nums[s],nums[e]]
                result.append(x)
                s+=1
                e-=1
            elif(current_sum >target):
                e-=1
            else:
                s+=1
    return result


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    target = int(input())
    result = triplets(arr,target)
    print(result)
    