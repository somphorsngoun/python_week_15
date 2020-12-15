studentsDictionary = eval(input())
newStudentsNumber= int(input())
newStudentsClass = input()

# Enter your code here. Read input from STDIN. Print output to STDOUT
if newStudentsClass == "2021D":
	studentsDictionary[newStudentsClass] = newStudentsNumber
for r in studentsDictionary:
    if newStudentsClass == r:
        result = "Class " + r + " has " + str(studentsDictionary[r]+newStudentsNumber) + " students"
    else:
        result = "Class " + r + " has " + str(studentsDictionary[r]) + " students"
    print(result)