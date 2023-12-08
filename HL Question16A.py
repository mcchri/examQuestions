# Question 16(a)
# Student Name: Christian Turean
# function to asks the username
def user_name():
    name = input("Please enter your username: ")
    print("Welcome",name,", to the student result calculator.")
#calls the function
user_name()
#inputs for the mark
student_name=input("Please enter the students name: ")
student_score=float(input("Please enter the students mark: "))
exam_total = int(input("Please enter the total amount of marks going for the exam: "))
#converts the mark into a percentage
score_as_a_percentage=(student_score/exam_total)*100
#rounds the percentage to 1 decimal place
score_as_a_percentage = round(score_as_a_percentage, 1)
#gives a grade depending on the percentage
if score_as_a_percentage > 79:
    grade = "A"
elif score_as_a_percentage >59:
    grade = "B"
else:
    grade = "C"
#the output is displayed    
print(student_name,"scored",score_as_a_percentage,"%. They got a",grade,".")



