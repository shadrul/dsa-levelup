# Longest Band Problem 

def longestBand(nums):
    s = set()
    for i in nums:
        s.add(i)
    longest = 0
    for i in nums:
        parent = i-1
        if parent not in s:
            next_ele = i+1
            count =1
            while(next_ele in s):
                next_ele+=1
                count+=1
            longest = max(longest,count)
    return longest
                


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    result = longestBand(arr)
    print(result)
    