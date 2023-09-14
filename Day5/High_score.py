student_scrore = input("Student Scores: ").split()
for n in range(0, len(student_scrore)):
    student_scrore[n] = int(student_scrore[n])
print(student_scrore)

highest_score = 0
for score in student_scrore:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}.")