#Part A - broken fix later
weeks = 16
classes = 5
tuition = 6000
classes_per_week = 3
cost_per_week = ((tuition / classes) / weeks)
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class)
#Part B