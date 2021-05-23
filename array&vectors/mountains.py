# Mountains 

def mountains(arr):
    largest = 0
    n = len(arr)
    i = 1
    while(i<n-1):
        if(arr[i] >arr[i-1] and arr[i] > arr[i+1]):
            count = 1
            j = i
            while(j>=1 and arr[j]>arr[j-1]):
                count+=1
                j-=1
            while(i<n-1 and arr[i]>arr[i+1]):
                count+=1
                i+=1
            largest = max(largest,count)
        else:
            i+=1
    return largest


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    result = mountains(arr)
    print(result)
    