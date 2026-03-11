answer = input("Input: ")

print("Output: ", end="")

for char in answer:
    if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(char, end="")

print()