#min Difference
import sys
def minDiff(a,b):
    al = len(a)
    bl = len(b)
    a.sort()
    b.sort()
    m= sys.maxsize
    i =j =0
    while(i<al and j<bl):
        if(abs(a[i]-b[j])<m):
            m = abs(a[i]-b[j])
            x = a[i]
            y = b[j]
        if(a[i]<b[j]):
            i+=1
        elif(a[i]>b[j]):
            j+=1
        else:
            x = a[i]
            y = b[j]
            return (x,y)
    return (x,y)        
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    result = minDiff(arr,arr1)
    print(result)