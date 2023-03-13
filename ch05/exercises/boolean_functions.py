def percentage_to_letter(score=0):
    if score >= 90: grade = "A"
    elif score >= 80: grade = "B"
    elif score >= 70: grade = "C"
    elif score >= 60: grade = "D"
    elif score < 60: grade = "F"
    return grade

def is_passing(letter):
    if letter == "A" or letter == "B" or letter == "C":
        passing = True
    else: passing = False
    return passing

def main():
    percentage = input("What's your percent grade? ")
    grade = percentage_to_letter(int(percentage))
    print("Letter Grade:", grade)
    passing = is_passing(grade)
    if passing: print("You passed! :D",)
    else: print("You failed! :o")

main()