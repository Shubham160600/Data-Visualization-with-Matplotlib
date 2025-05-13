import matplotlib.pyplot as plt

x = ['Jan', 'Feb', 'Mar', 'Apr']
y = [1000, 1200, 900, 1500]

plt.plot(x, y, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()
