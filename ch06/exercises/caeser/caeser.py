#i think i got sick during this class if it was march 16 so its just me

import json

def code(filepath, codedict, incrementation):
    file = open(filepath, "r")
    string = file.read()
    newstring = ""
    file.close()
    file = open("/Users/School/github-classroom/bucs110SPRING23/portfolio-bbulger1/ch06/exercises/caeser/newcode.txt", "w")
    for x in range(0, len(string), incrementation):
        if incrementation == 2: codeinput = string[x] + string[x + 1]
        else: codeinput = string[x]
        newx = codedict.get(codeinput)
        newstring = newstring + newx
    file.write(newstring)
    print(newstring)

def main():
    jsonimport = open("/Users/School/github-classroom/bucs110SPRING23/portfolio-bbulger1/ch06/exercises/caeser/cypher.JSON")
    codedict = json.load(jsonimport)
    inv_codedict = {v: k for k, v in codedict.items()}
    filepath = "/Users/School/github-classroom/bucs110SPRING23/portfolio-bbulger1/ch06/exercises/caeser/code.txt"
    print("Select 1 to decode coded file. Select 2 to code uncoded file.")
    option = input("Selection: ")
    if option == "1": code(filepath, codedict, 2)
    if option == "2": code(filepath, inv_codedict, 1)

main()