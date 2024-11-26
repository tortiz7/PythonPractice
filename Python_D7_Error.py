
try:
    with open('unknown.txt', 'r') as f:
        for i, line in enumerate(f):
            print(f"{i+1}: {line.strip()}")
except FileNotFoundError as e:
    print(f"Opening that document gave this error: {e}")