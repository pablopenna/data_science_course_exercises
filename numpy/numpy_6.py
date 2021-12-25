import numpy as np

data = np.loadtxt('./datos.txt')

# Average of populations across all time
a = data[:,1:].mean(axis=0)
print(f"mean: {a}")

# Standard deviation
b1 = np.std(data[:,1:], axis=0)
print(f"tandard deviation: {b1}")
# also
b2 = data[:,1:].std()
print(f"tandard deviation: {b2}")

# Sum of the populations for each year
c= np.sum(data,axis=0)[1:]
print(f"sum: {c}")

# max of each population
d1 = data[:,1:].max(axis=0) #Max values
d2 = data[:,1:].argmax(axis=0) #Indexes for each column for where to find the max value

# Which species has had more population per year
e1 = data[:,1:].max(axis=1) # value of highest population
e2 = data[:,1:].argmax(axis=1) # highest population
