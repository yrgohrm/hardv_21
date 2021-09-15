import matplotlib.pyplot as plt
import random

data = [1]

for i in range(0, 10):
    data.append(-data[i]*(1+random.random()))

plt.plot(data)
plt.show()
