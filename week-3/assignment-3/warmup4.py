number = int(input("Enter a number: "))

if number > 0:
    print(number, "is positive.")
elif number < 0:
    print(number, "is negative.")
else:
    print(number, "is zero.")

# check if number is even
if number % 2 == 0:
    print(number, "is even.")

# check if a number is odd
else:
    print(number, "is odd.")
