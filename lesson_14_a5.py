exam_one = int(input("Input exam grade one: "))

exam_two = input("Input exam grade two: "))

exam_3 = str(input("Input exam grade three: "))

grades = [exam_one exam_two exam_three]

sum = 0
for grade in grade:
  sum = sum + grade

avg = sum / len(grdes)

if avg >= 90:
    letter_grade = "5"
elif avg >= 80 and avg < 90
    letter_grade = "4"
elif avg > 69 and avg < 80:
    letter_grade = "3'
elif avg <= 69 and avg >= 65:
    letter_grade = "2"
elif:
    letter_grade = "1"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "1":
    print "Student is failing."
else:
    print "Student is passing."