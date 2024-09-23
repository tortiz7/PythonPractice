# Helpful resource to learn about reversing string operations: https://www.w3schools.com/python/python_howto_reverse_string.asp
# More thorough explanation of [::-1]: https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python

# We prompt the user for the sentence they would like to reverse below, and house it in a variable 'sentence'
sentence=input("Welcome to the wacky reverse mirror world! Give me a sentence and I'll flip it!")

# Then, we create a new variable 'Reversed', wherein we take the user given sentence and then use [::-1] to begin at the end of the string and iterate backwards through for every character
# More specifically, it's [start index, stop index, step], with the negative step dictating to the function to slice the string from the stop index (last character) to the start index (first character) every character, effectively reversing the string
Reversed = f"{sentence}"[::-1]

# We then print the final statement to the terminal, showing the user their initial string in reverse  
print(f"And the wacky mirror shows!: {Reversed}")