# Write a Python script that reads from a text file named data.txt and prints each line with its line number. Test Script by creating a data.txt file

try:
    with open('data.txt', 'r') as f:
        for i, line in enumerate(f):
            print(f"{i+1}: {line.strip()}")
except FileNotFoundError as e:
    print(f"Opening that document gave this error: {e}")
    