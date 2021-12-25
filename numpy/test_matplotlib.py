import matplotlib.pyplot as plt
import numpy as np

arr = np.random.randint(2,5,10)
indices = [1,2,3,4,5,6,7,8,9,10]
fig, ax = plt.subplots()
ax.plot(indices, arr)
plt.show()
