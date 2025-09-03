


def twosum(arr, target):
  ht=dict()
  for val in arr:
      c = target-val
      if not ht.get(val):
           ht[c] = 1
      else:
           return c, val
         
  return -1,-1

arr = [2,4,6,7]
target = 11
ret = twosum(arr, target)
print (ret)