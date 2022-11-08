import pandas as pd

a = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(a)

print(a[:2])
print("\nc   ",a["c"],"\n")
print(a[-2:])

dict = {"a":1,"b":2,"c":3,"d":4,"e":5}
b = pd.Series(dict, index=["c","b","X","a","d","e"])
print(b)
print(b["c"])
print(b.count(),'aa')
print(b.size)

c = pd.Series([[1, 2, 3], 'foo', [], [3, 4]])
print(c.explode(ignore_index = True))

d = pd.Series([4+3j,-1,4,1.3+3j])
print(d.abs())