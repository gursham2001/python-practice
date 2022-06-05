continue_calculating = "Y"

while continue_calculating == "Y" or continue_calculating == "y":
    num1 = float(input("Input first num: "))
    operator = input("choose operator +, -, /, * : ")
    num2 = float(input("Input second num: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)

    continue_calculating = input("Continue calculations?: Y or N: ")

print("Thanks for calculating today")