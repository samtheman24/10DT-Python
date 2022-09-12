# S R Jones
# input, out, else, elif, if

# provide instruction to the user
# prompt user for input

print("select the operation to preform: ")
print("1.  ADD")
print("2.  SUBTRACT")
print("3.  MULTIPLY")
print("4.  DIVIDE")

operation = input()

if operation == "1":
    # code for add
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the sum is " + str(int(num1) + int(num2) + "."))

elif operation == "2":
    # code for subtract
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the sum is " + str(int(num1) - int(num2) + "."))

elif operation == "3":
    # code for multiply
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the sum is " + str(int(num1) * int(num2) + "."))

elif operation == "4":
    # code for add
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the sum is " + str(int(num1) / int(num2) + "."))

else:
    print()




