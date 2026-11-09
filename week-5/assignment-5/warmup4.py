# We go numbers 1 - 30
# Then, we check if each number is divisible by 3 and 5. 
# If the number is divisible by 3 & 5, prints "FizzBuzz"
# If the number is divisible by 3, print "Fizz"
# If the number is divisible by 5, print "Buzz"
# If the number is not divisible by 3 and 5, tell python 
# to print the number. 

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)       
        
