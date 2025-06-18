from calculator.add import add
from calculator.sub import sub
from calculator.multiply import multiply
from calculator.divide import divide

if __name__ == "__main__":
    a = 10
    b = 5

    print("Add: ", add(a, b))
    print("Sub: ", sub(a, b))
    print("Multiply: ", multiply(a,b))
    print("Divide: ",divide(a,b))