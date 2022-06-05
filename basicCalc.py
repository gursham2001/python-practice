print("choice 1 = +")
print("choice 2 = -")
print("choice 3 = *")
print("choice 4 = /")

n1 = float(input("First number: "))
operator = input("Enter your choice of operator: ")
n2 = float(input("Second number: "))

# n1 = 4
# operator = "+"
# n2 = 2

def adding():
    print(n1 + n2)
    return
def subtract():
    print(n1 - n2)
    return
def multiply():
    print(n1 * n2)
    return
def divide():
    print(n1 / n2)
    return

if operator == "+":
    adding()
elif operator == "-":
    subtract()
elif operator == "*":
    multiply()
elif operator == "/":
    divide()
else:
    print("Invalid operator")

    # def adding():
    #     return(n1 + n2)
    # def subtract():
    #     return(n1 - n2)
    # def multiply():
    #     return(n1 * n2)
    # def divide():
    #     return(n1 / n2)

    # if adding():
    #     print(adding)
    # elif subtract():
    #     print(subtract)
    # elif multiply():
    #     print(multiply)
    # elif divide():
    #     print(divide)

    # adding(2,3)
    # calculate(adding(2,4))