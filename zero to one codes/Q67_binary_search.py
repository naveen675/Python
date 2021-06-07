

def binary(arr,n):          #Iterative Way

    r = len(arr)-1
    l =0
    mid = (l+r)//2
    while l<=r:
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            r = mid-1
            mid = (l+r)//2
        elif arr[mid] < n:
            l = mid+1
            mid = (l+r)//2
    return -1

def binary(arr,l,r,x):        #Recursive way,works only till 1000

    mid = l + (r-1)//2

    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary(arr,l,mid-1,x)
    elif arr[mid] < x:
        return binary(arr,mid+1,r,x)
    return -1


if __name__ == '__main__':
    arr = [*range(10000000)]
    #print(arr)
    print(binary(arr,786000))

    #print(binary(arr,0,len(arr)-1,7865))

