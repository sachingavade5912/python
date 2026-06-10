num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))


def calculator(user_input):
    operation = user_input.strip().lower()

    match operation:
        case "addition":
            print(num1 + num2)

        case "subtraction":
            if num2 > num1:
                print("Number 2 is greater than Number 1; cannot perform subtraction")
            else:
                print(num1 - num2)
        case "multiplication":
            print(num1 * num2)
        case "division":
            print(num1 * num2)
        case _:
            print("Invalid operation selection")
        

while True:
    input_operation = input("\nPlease enter a operation to perform: ")
    if input_operation.lower() == "quit":
        break
    calculator(input_operation)




