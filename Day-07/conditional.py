import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Creating t2.micro instance")
elif type == "t3.micro":
    print("Creating t3.micro instance")
else:
    print("Provide correct instance type")