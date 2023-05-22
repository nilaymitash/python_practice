def checkIfPlaindrome(str):
    length = len(str)
    for index in range(0, length):
        if(str[index].casefold() != str[length- 1 - index].casefold()):
            return False
    return True

user_input = input("Enter a string.\n");
if(checkIfPlaindrome(user_input)):
    print("%s, is a palindorme." %user_input)
else:
    print("%s, is NOT a palindorme." %user_input)