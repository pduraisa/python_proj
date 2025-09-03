


def twosum(arr, target):
  ht=dict()
  for val in arr:
      c = abs(target-val)
      if val in ht.values():
           return c, val
      else:
         ht[val]=c
  return -1,-1

arr = [2,4,6,7]
target = 10
ret = twosum(arr, target)
print (ret)