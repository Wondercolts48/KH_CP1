# Kh 2nd flexible calculator

"""
PSEUDOCODE:

1. Import necessary modules (statistics for average)

2. Define calculator function:
   - Accept *args for any number of values
   - Accept operation parameter (default or **kwargs)
   - Use conditional logic to determine which operation to perform
   - Return the result

3. Define function to display menu:
   - Show available operations
   - Return user's choice

4. Define function to collect numbers:
   - Loop until user indicates they're done
   - Convert input to float
   - Add to list of numbers
   - Return list

5. Define main function:
   - Display menu and get operation choice
   - Collect numbers from user
   - Call calculator function with numbers and operation
   - Display result in readable format
   - Ask if user wants to perform another calculation

6. Run main function
"""

import statistics

def calculator(*args, operation='sum'):
    """
    Performs calculations on any number of values.
    
    Args:
        *args: Variable number of numeric values
        operation: String specifying the operation (sum, average, max, min, product)
    
    Returns:
        The result of the specified operation
    """
    if not args:
        return "Error: No numbers provided"
    
    if operation == 'sum':
        return sum(args)
    elif operation == 'average':
        return statistics.mean(args)
    elif operation == 'max':
        return max(args)
    elif operation == 'min':
        return min(args)
    elif operation == 'product':
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "Error: Invalid operation"


def display_menu():
    """
    Displays the menu of available operations and gets user's choice.
    
    Returns:
        String representing the chosen operation
    """
    print("\n" + "="*50)
    print("FLEXIBLE CALCULATOR")
    print("="*50)
    print("\nAvailable Operations:")
    print("  1. Sum       - Add all numbers together")
    print("  2. Average   - Calculate the mean")
    print("  3. Max       - Find the largest number")
    print("  4. Min       - Find the smallest number")
    print("  5. Product   - Multiply all numbers together")
    print("="*50)
    
    operations = {
        '1': 'sum',
        '2': 'average',
        '3': 'max',
        '4': 'min',
        '5': 'product'
    }
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice in operations:
            return operations[choice]
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


def collect_numbers():
    """
    Collects numbers from the user until they're done.
    
    Returns:
        List of float numbers entered by the user
    """
    numbers = []
    print("\n" + "-"*50)
    print("Enter numbers (type 'done' when finished)")
    print("-"*50)
    
    while True:
        user_input = input(f"Enter number {len(numbers) + 1} (or 'done'): ").strip()
        
        if user_input.lower() == 'done':
            if numbers:
                break
            else:
                print("You must enter at least one number!")
                continue
        
        try:
            number = float(user_input)
            numbers.append(number)
            print(f"  ✓ Added: {number}")
        except ValueError:
            print("  ✗ Invalid input! Please enter a valid number or 'done'.")
    
    return numbers


def display_result(operation, numbers, result):
    """
    Displays the calculation result in a readable format.
    
    Args:
        operation: The operation performed
        numbers: List of numbers used
        result: The calculated result
    """
    print("\n" + "="*50)
    print("RESULT")
    print("="*50)
    print(f"Operation: {operation.upper()}")
    print(f"Numbers: {', '.join(map(str, numbers))}")
    print(f"Result: {result}")
    print("="*50)


def main():
    """
    Main function that runs the calculator program.
    """
    print("\n🔢 Welcome to the Flexible Calculator! 🔢")
    
    while True:
        # Get operation choice
        operation = display_menu()
        
        # Collect numbers from user
        numbers = collect_numbers()
        
        # Perform calculation
        result = calculator(*numbers, operation=operation)
        
        # Display result
        display_result(operation, numbers, result)
        
        # Ask if user wants to continue
        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n✨ Thank you for using the Flexible Calculator! Goodbye! ✨\n")
            break


# Run the program
if __name__ == "__main__":
    main()
