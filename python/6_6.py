
d = {1: "Roma", 2: "Milan", 3: "Napoles", 4: "Turin", 5: "Palermo", 6: "Genova", 7: "Bolonia", 8: "Florencia", 9: "Bari", 10: "Catania"}
pob = [2718768, 1299633, 973132, 908263, 663173, 610887, 372256, 364710, 322511, 298957]

cities = list(d.values())

# Change keys to values and set population as values
res1 = {d[k]:pob[idx] for idx, k in enumerate(d)}
print(f"res1: {res1}")

# Add population to dict
res2 = {k:[d[k], pob[idx]] for idx, k in enumerate(d)}
print(f"res2: {res2}")
