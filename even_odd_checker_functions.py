def get_integer_input() -> int:
    """
    Prompts the user to enter an integer and validates the input.

    Returns:
        int: The validated integer input.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines whether a given number is even or odd.

    Parameters:
        number (int): The integer to check.

    Returns:
        str: A message indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """
    Main function to get user input and check if the number is even or odd.
    """
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
