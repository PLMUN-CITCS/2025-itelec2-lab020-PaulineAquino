"""
This script prompts the user for an integer and determines if it's even or odd.
It includes functions for input validation and even/odd checking.
"""

def get_integer_input() -> int:
    """
    Prompts the user to enter an integer and validates the input.

    Returns:
        int: The validated integer input.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number  # Return only after successful conversion
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Loop continues after error

def check_even_odd(number: int) -> str:
    """
    Determines whether a given number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."  # Removed unnecessary 'else'

def main() -> None:
    """
    Main function to get user input and check if the number is even or odd.
    """
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
