import random

#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class)

#Part B
the_list = ["cool", "fail", 1, 4, 0.0013516167]
the_pick = random.choice(the_list)
print("Today's pick is...", the_pick)