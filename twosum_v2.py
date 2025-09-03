


def twosum(arr, target):
  tb=dict()
  for val in arr:
      c = target-val
      if c not in tb:
           tb[val] = 1
      else:
           return c, val
         
  return -1,-1

arr = [2,4,6,7]
target = 10
ret = twosum(arr, target)
print (ret)