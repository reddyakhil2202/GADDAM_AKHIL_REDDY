# Problem-1: 
# Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
# Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
# Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid Operation"


calc1 = Calculator(10, 5, "add")
calc2 = Calculator(10, 5, "sub")
calc3 = Calculator(10, 5, "mul")
calc4 = Calculator(10, 5, "div")
print("Result:", calc1.calculate())
print("Result:", calc2.calculate())
print("Result:", calc3.calculate())
print("Result:", calc4.calculate())
