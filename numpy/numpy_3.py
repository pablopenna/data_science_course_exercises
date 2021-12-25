import numpy as np

a = np.zeros(20, dtype=np.int8)
a[:5]=10

b = np.arange(12,32,2,dtype=np.int8)

a[5:15] = b

print(f"res{a}")
