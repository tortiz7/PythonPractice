# Resources that aided in the learning for this scripting challenge: https://www.programiz.com/python-programming/examples/odd-even
# And: https://www.tutorialspoint.com/how-do-i-check-if-raw-input-is-integer-in-python-3#:~:text=%23%20Prompt%20user%20for%20input%20user_input,input%20is%20not%20an%20integer.

# We begin with a While loop (my faves!), so we can force the script to restart if the user inputs a string that cannot be converted into an integer

while True:
    # We use try here for error handling - if the string cannot be converted to an integer, then a "ValueError" exception will be raised, and the user will be taken to the beginning of the script
    try: 
        # line 10 asks the user to input their number, and then converts the string they've inputted into an integer for our if conditional
        num=int(input("Wow, you seem to have bumped your head and no longer know the difference between even and odd numbers. Let me help you buddy! Give me a number:"))
        if num % 2 == 0: # the "%" is a modulous operator, which returns the remainder after two numbers are divided by eachother. In the context of the script, it's checking in the number given by the User can be divided by 2 without a remainder (== 0). If it can, then it's even and the print statement will say so. if there is a remainder, then it's odd. 
            print(f"{num} is an even number!")
        else: 
            print(f"{num} is an odd number!")
        try_again=input("Want to test with another number? y/n: ").casefold() # We ask the User if they would like to see if other numbers are even or odd, and save that to the "try_again" variable. Note our old friend case.fold(), to keep their answers case insensitive
        if try_again == "y":
            continue # If "try_again" is equal to "y", then the script restarts. If it's anything but "y", the script will break. 
        else:
            break
    except ValueError:
        print("That's not a number - you must've bumped your head hard! Please give me a number") # Here's the error handling message that works in conjunction with "try" and the "except ValueError" exception. "ValueError" is an exception that is raised by when an argument is correct but does not work for the stated function. In the context of our script, a string is a correct argument, but one containing words or special characters cannot be converted by int into an integer, hence the "ValueError"
        continue
