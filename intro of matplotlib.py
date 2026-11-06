import matplotlib.pyplot as plt

days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
scores = [56, 67, 35, 34, 78]

plt.plot(days, scores)
plt.show()

plt.plot(days, scores)
plt.title("Quiz scores")
plt.xlabel("week days")
plt.ylabel("scores")
plt.grid(True)
plt.show()

plt.plot(days, scores, color="black", marker="x", linestyle="dashed")
plt.xlabel("week days")
plt.ylabel("scores")
plt.show()

plt.bar(days, scores, color="green")
plt.title("Quiz scores")
plt.xlabel("week days")
plt.ylabel("scores")
plt.grid(True)
plt.show()
           
