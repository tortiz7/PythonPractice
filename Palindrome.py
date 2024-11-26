Pal = input("Let's see if this word is a palindrome!: ")

Lap = Pal[::-1]

if Pal == Lap:
    print(f"{Pal} is {Pal} reversed! It's a Palindrome!")
else: 
    print(f"{Pal} is {Lap} reversed...it's just a boring word :( ")