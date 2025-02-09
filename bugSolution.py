def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (will now work correctly):
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"The average is: {average}") 