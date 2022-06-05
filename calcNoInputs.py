#! need to complete

def calc(n1, n2):

    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def divide(n1, n2):
        return n1 / n2

    def multiply(n1, n2):
        return n1 * n2

    calc.add = add
    calc.divide = divide
    calc.subtract = subtract
    calc.multiply = multiply
    return

calc.add(2,5)