def check_even_odd(num: int) -> str:
    """
    Determine if a number is even or odd.
    """
    # Use modulus to check remainder when divided by 2
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
def check_sign(num: int) -> str:
    """
    Determine the sign of a number.
    """
    # Check different ranges of the number
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
def find_square(num: int) -> int:
    """
    Calculate the square of a number.
    """
    # Square means multiplying the number by itself
    return num ** 2
def find_cube(num: int) -> int:
    """
    Calculate the cube of a number.
    """
    # Cube means multiplying the number three times
    return num ** 3
def main():
    """
    Main function.
    - Takes input
    - Calls helper functions
    - Prints results
    """
    # Prompt the user to enter an integer
    num = int(input("Enter a number: "))

    # Call the functions and store results
    parity = check_even_odd(num)   # Even or Odd check
    sign = check_sign(num)         # Positive, Negative, or Zero
    square = find_square(num)      # Calculate square
    cube = find_cube(num)          # Calculate cube

    print("\nResults:")
    print("Number:", num)
    print("Even/Odd:", parity)
    print("Positive/Negative:", sign)
    print("Square:", square)
    print("Cube:", cube)


# Run the main function
if __name__ == "__main__":  
    main()
