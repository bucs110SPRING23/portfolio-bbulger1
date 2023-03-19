file = "/Users/School/github-classroom/bucs110SPRING23/portfolio-bbulger1/ch06/exercises/myideas.txt"

myideas = open(file)
pastidea = myideas.read()
print(pastidea)

myideas = open(file, "w")
idea = input("Idea: ")
myideas.write(idea)
myideas.close()