import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
pocket_money = [50, 80, 120, 160, 90, 250]

plt.plot(months, pocket_money)
plt.show()

plt.plot(months, pocket_money)
plt.title('My Pocket Money Growth')
plt.xlabel('Months')
plt.ylabel('Amount')
plt.grid(True)
plt.show()

plt.plot(months, pocket_money, color='purple', marker='s', linestyle='dotted', linewidth=3)
plt.title('My PocketMoney Growth')
plt.xlabel('Months')
plt.ylabel('Amount')
plt.grid(True)
plt.show()

plt.bar(months, pocket_money, color='green')
plt.title('Monthly Pocket Money Bar Chart')
plt.xlabel('Months')
plt.ylabel('Amount')
plt.show()