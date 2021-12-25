import numpy as np

arr = np.zeros(20).astype(np.int8)
# https://stackoverflow.com/questions/19666626/replace-all-elements-of-python-numpy-array-that-are-greater-than-some-value
# Solution in link does not really applies but still it is interesting
arr[:5]=10

print(f"res{arr}")
