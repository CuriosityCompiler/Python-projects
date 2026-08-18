print("Calculator")
print('1 Addition 2 Subtraction 3 Multiplication 4 Division')
operation = int(input("Select Operation (1-4): "))

if operation == 1:
        num1 = (float(input("Enter your first number: ")))
        num2 = (float(input("Enter your second number: ")))
        result = num1+num2
        print("The result of addition is: ", result)
elif operation == 2:
        num1 = (float(input("Enter your first number: ")))
        num2 = (float(input("Enter your second number: ")))
        result = num1-num2
        print("The result of subtraction is: ", result)
elif operation == 3:
        num1 = (float(input("Enter your first number: ")))
        num2 = (float(input("Enter your second number: ")))
        result = num1*num2
        print("The result of multiplication is: ", result)
elif operation == 4:
        num1 = (float(input("Enter your first number: ")))
        num2 = (float(input("Enter your second number: ")))
        if num2 != 0:
            result = num1/num2
            print("The result of division is: ", result)
else:
        print("Error: Division by zero is not allowed.")
