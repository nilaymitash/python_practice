def fizzBuzz_basic():
    for i in range(1, 101):
        isDivBy3 = i%3 == 0
        isDivBy5 = i%5 == 0
        if(isDivBy3 and isDivBy5):
            print("fizzbuzz")
        elif(isDivBy3):
            print("fizz")
        elif(isDivBy5):
            print("buzz")
        else:
            print(i)

def fizzBuzz_efficient():
    # hint: No modulus operator; every 3rd and 5th number is fizz, buzz, or fizzbuzz
    third = 0
    fifth = 0
    for i in range(1, 101):
        third += 1
        fifth += 1
        fb = ""
        if(third == 3):
            fb += "fizz"
            third = 0
        if(fifth == 5):
            fb += "buzz"
            fifth = 0
        if(fb is not ""):
            print(fb)
        else: 
            print(i)



#fizzBuzz_basic()
fizzBuzz_efficient()