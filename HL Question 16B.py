# Question 16(b)
# examination Number: Christian Turean
#function for the name list
def student_name_funct():
    student_name_list = []
    student_name = ""
    ok = 0
    while ok != -1:
        student_name = input("Please enter the students name and enter 'end' or 'End' when complete: ")
        if student_name == "end" or student_name == "End":
            ok = -1
            return student_name_list
        else:
            student_name_list.append(student_name)
#function to store all results in a list
def student_grade_funct():
    student_grade_list = []
    student_grade = 0
    ok = 0
    while ok != -1:
        student_grade = int(input("Please enter the students result and enter '-1' when complete: "))
        if student_grade == -1:
            ok = -1
            return student_grade_list
        else:
            student_grade_list.append(student_grade)
name_list = student_name_funct()
print("")
result_list = student_grade_funct()
print("")
#prints out the lists
print("Student names are:",name_list)
print("Student results are:",result_list)
#if the length of both lists are unequal, follow some actions
if len(name_list) < len(result_list):
    print("ERROR: You have entered more students results than students names \n Compare the entered names and results and add the missing name to the correct index location")
    print("")
    print("Student results are:",result_list)
    print("")
    print("Student names are:",name_list)
    print("")
    miss_name = input("Please enter the students name that was left out: ")
    index = int(input("What is the index position of the name: "))
    name_list.insert(index, miss_name)
    #name_list[index] = miss_name
elif len(name_list) > len(result_list):
    print("ERROR: You have entered more students names than students results \n Compare the entered names and results and add the missing result to the correct index location")
    print("")
    print("Student results are:",result_list)
    print("")
    print("Student names are:",name_list)
    print("")
    miss_result = int(input("Please enter the students result that was left out: "))
    index = int(input("What is the index position of the result: "))
    result_list.insert(index, miss_result)
    #result_list[index] = miss_result
count = 0
print("")
#reveals the highest and lowest score
high_score = (max(result_list)/200)*100
print("Highest value scored is:",high_score,"%")
low_score = (min(result_list)/200)*100
print("Lowest value scored is:",low_score,"%")
print("")
#shows what students
print("The student who scored the highest value is:",name_list[result_list.index(max(result_list))])
print("The student who scored the lowest value is:",name_list[result_list.index(min(result_list))])
avg_score = ((sum(result_list)/200)*100)/2
#prints the average score
print("The average value in the class is:",avg_score,"%")

    