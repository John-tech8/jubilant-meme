import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker='o')
plt.annotate("Maximum Sales",
             xy=(4, 30),
             xytext=(2.5, 32),
             arrowprops=dict(arrowstyle="->"))

plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Analysis")
plt.show()
