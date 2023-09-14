#Average height exercise

# Initialize total to 0
total = 0

# Initialize count to 0 to keep track of the number of heights
count = 0

# Input a list of student heights and split them
students_heights = input("Input a list of student heights: ").split()

# Convert the input values to integers
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

# Calculate the sum of heights and count the number of heights
for num in students_heights:
    total += num
    count += 1

# Calculate the average height
average = round(total / count)

# Print the average height
print("The average height is:", average)

