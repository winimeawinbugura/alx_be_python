# pattern_drawing.py
# A program that draws a square pattern using nested loops.

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after finishing a row
    row += 1
