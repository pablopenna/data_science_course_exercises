
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
res = []

for i in range(len(abc)):
    if (i+1)%3!=0:
        res.append(abc[i])

print(f"abc: {abc}")
print(f"res: {res}")