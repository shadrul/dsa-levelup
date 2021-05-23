# Rain Water Trapping SOlution in O(n)

def rainWater(height):
    m = -1
    n = len(height)
    if(n<2):
        return 0
    l = [0]*n
    r = [0]*n
    for i in range(n):
        m = max(height[i],m)
        l[i] = m
    m = -1
    for i in range(n-1,-1,-1):
        m = max(height[i],m)
        r[i] = m
    s = 0
    for i,v in enumerate(height):
        temp = min(l[i],r[i])-v
        s+=temp
    return s
                


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    result = rainWater(arr)
    print(result)
    