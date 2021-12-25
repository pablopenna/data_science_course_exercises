l1 = [1,2,3,17,4,5,6]
l2 = [1,51,2,3,5,1,17]
common = []

for e in l1:
    if e in l2:
        common.append(e)

print(f"elements in common: {common}")
