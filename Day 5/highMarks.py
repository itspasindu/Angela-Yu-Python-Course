student_scores = [15, 50, 60, 70, 11, 89, 87, 47, 38, 50, 98, 74, 53, 89, 91, 69, 72, 42]

total = sum(student_scores)
print(total)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)