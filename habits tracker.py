habit = ("Traveling", True, 38, 5.5)

weekly_habits = (1, 0, 1, 1, 0, 1, 1)

total_days = len(weekly_habits)
print("Total days:", total_days)

print("Day 1 status:", weekly_habits[0])
print("Day 4 status:", weekly_habits[3])

print("First 3 days:", weekly_habits[0:3])
print("Last 2 days:", weekly_habits[5:7])

new_weekly_habits = weekly_habits + (1,)
print("Updated Day 8:", new_weekly_habits)

completed = weekly_habits.count(1)
missed = weekly_habits.count(0)

completed = 0
missed = 0

for day in weekly_habits:
    if day == 1:
        completed = completed + 1
    else:
        missed = missed + 1

print("Completed Days:", completed)
print("Missed Days:", missed)

if completed > missed:
    print("Awesome job")
else:
    print("Keep going")