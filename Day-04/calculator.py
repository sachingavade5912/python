num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))


def calculator(user_input):
    operation = user_input.strip().lower()

    match operation:
        case "addition":
            sum = num1 + num2
            return sum

        case "subtraction":
            if num2 > num1:
                print("Number 2 is greater than Number 1; cannot perform subtraction")
            else:
                sub = num1 - num2
                return sub

        case "multiplication":
            mul = num1 * num2
            return mul

        case "division":
            div = num1 / num2
            return div

        case _:
            print("Invalid operation selection")
        

while True:
    input_operation = input("\nPlease enter a operation to perform: ")
    if input_operation.lower() == "quit":
        break
    result = calculator(input_operation)
    print(result)




