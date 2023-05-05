def printme(string):
    "This prints whatever is passed in"
    print(string)
    return;

def fizzBuzz(number):
    for i in range(1, number+1):
        print(i)
        if(i%2 == 0):
            print("even")
        else:
            print("odd")

def factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial;

def factorialRecursive(number):
    if(number == 1):
        return number;
    if(number > 1):
        return number * factorialRecursive(number - 1)

num = int(input("Enter a number.\n"))
#fizzBuzz(num)
print("Factorial of " + str(num) + " is: " + str(factorialRecursive(num)))