import random

def main():
    level = get_positive_int("Level: ")
    target = random.randint(1, level)

    while True:
        guess = get_positive_int("Guess: ")
        
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass

if __name__ == "__main__":
    main()