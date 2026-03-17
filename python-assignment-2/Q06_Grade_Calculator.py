# Question 6: Grade Calculator
"""
Ask users for marks in 5 subjects (out of 100 each). Calculate and display:
1. Marks in each subject
2. Total marks (out of 500)
3. Percentage
4. Grade
5. Result: Pass/Fail (Pass if all subjects >= 40)
"""

# Take user input
marks = []
for i in range(1,6):
    subject_marks = float(input(f"Enter marks for Subject {i} (out of 100): "))
    marks.append(subject_marks)

# Display marks in each subject
print("\nMarks in each subject: ")
for i in range(5):
    print(f"Subject {i+1}: {marks[i]}")

# Calculate Total marks
total_marks = sum(marks)
print(f"Total marks (out of 500): {total_marks}")

# Calculate Percentage
percentage = total_marks / 5
print(f"Percentage: {percentage}")

# Deterine Grade
if percentage >= 90:
    print("Grade: A+ (Outstanding)")
elif percentage >= 80:
    print("Grade: A (Excellent)")
elif percentage >= 70:
    print("Grade: B (Good)")
elif percentage >= 60:
    print("Grade: C (Average)")
elif percentage >= 50:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")

# Display Result
if all(mark >= 40 for mark in marks):
    print("Result: Pass")
else:
    print("Result: Fail")