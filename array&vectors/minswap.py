# Sort array by swaapng minimum number of times
import sys
def minSwap(nums):
    l = []
    for i,v in enumerate(nums):
        l.append((i,v))
    
    l.sort(key = lambda l:l[1])
    visited = [False for i in range(len(l))]

    res = 0
    for i in range(len(l)):
        # if node is visited or element already at correct place then continue
        old_pos = l[i][0]
        if(old_pos == i or visited[i]):
            continue
        
        cycle = 0
        j = i
        while(visited[j] == False):
            visited[j] = True
            j = l[j][0]
            cycle+=1
        
        if(cycle>0):
            res+=cycle-1
    return res
        
        


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    result = minSwap(arr)
    print(result)
    