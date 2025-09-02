

def twosum(arr, target):
    n=len(arr)
    for idx1 in range(n):
        for idx2 in range(idx1+1,n):
            if arr[idx1] + arr[idx2] == target:
                return idx1,idx2
    return -1, -1
            
arr = [2,4,5,6,7]
target = 6
ret = twosum(arr, target)
print(ret)

            
