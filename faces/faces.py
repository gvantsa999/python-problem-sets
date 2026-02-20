def main():
    # Get user input
    user_input = input("Say something: ")
    
    # Convert the input using our function
    result = convert(user_input)
    
    # Print the final result
    print(result)

def convert(text):
    # Replace :) with 🙂
    # Replace :( with 🙁
    # The .replace() method returns a new version of the string
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    
    return text

# Call main at the bottom
if __name__ == "__main__":
    main()