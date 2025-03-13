# Initialize the sum variable
total_sum = 0

# Start an infinite loop
while True:
    # Prompt user for input
    user_input = input("Enter a number (or 'stop' to finish): ").strip().lower()
    
    # Check if the sentinel value 'stop' is entered
    if user_input == "stop":
        break  # Exit the loop

    # Try to convert input to a number and add to total_sum
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")

# Print the final total sum
print("The total sum is:", total_sum)
