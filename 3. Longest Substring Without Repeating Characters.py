s = "abcabcbb"
sep = list(s)
print(sep)
item = []
for i in sep:
    result = 0
    for j in sep:
        if i != j:
            result += 1 
    item.append(result)
print(max(item))