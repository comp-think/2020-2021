#----(matplot intro)
import matplotlib.pyplot as plt

data = [23,85, 72, 43, 52]
labels = ['A', 'B', 'C', 'D', 'E']

# x-Axis ticks and label
plt.xticks(range(len(data)), labels)
plt.xlabel('Class')

# y-Axis label
plt.ylabel('Amounts')

# chart title
plt.title('I am title')

# plt a bar
plt.bar(range(len(data)), data)
plt.show()
