# Pair Sum using set in O(n)

def pairSum(arr,target):
    x = set()
    for i,v in enumerate(arr):
        check = target - v
        if check in x: #lookup in set in O(1)
            a = i+1
            b = arr.index(check) +1
            return sorted([a,b])
        x.add(v)


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    target = int(input())
    result = pairSum(arr,target)
    print(result)
    