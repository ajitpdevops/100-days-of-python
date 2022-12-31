student_scores = input("Enter the a list of scores for a student: ")
# E.g. 78, 51, 91, 97, 95, 51, 63, 45

score_list = student_scores.split(", ")

score_list_int = []

for n in range(0, len(score_list)):
    score_list[n] = int(score_list[n])
    score_list_int.append(score_list[n])

print(score_list_int)

'''
# If I would not know the max() function

high_score = 0
for score in score_list_int:
    if score > high_score:
        high_score = score
'''

high_score = max(score_list_int)
low_score = min(score_list_int)


print(f"The highest score in the class is: {high_score}")
print(f"The lowest score in the class is: {low_score}")
