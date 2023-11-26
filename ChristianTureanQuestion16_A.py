# Question 16(a)
# Name and School: Christian Athlone Community College
#question a
import random
aux = "RETURN"
# here is the while loop
while aux != "END":
    #here is all the input
    s_name=input("Enter your surname:      ")    
    f_name=input("Enter your first name:      ")
    age=input("Enter your age:      ")
    eir = input("Eircode is:      ")
    
    trial = input("Do you agree to enroll in a vaccine trial? \n Type \'Yes\' or \'No\'        ")
    lis = ["A","B","C"]
    # This function chooses randomly out of the list
    select = random.choice(lis)
    
    print("Hello", f_name, s_name, "you are",age,"years old and your \n Eircode is",eir)
    
    # turning the eir code to a list then taking the last element and turning it into a int
    eir = list(eir)
    loc = ""
    first = eir[-1]
    first = int(first)
    # Checking if the last element is odd or even
    if first %2 != 0:
        loc = "Northfield"
    else:
        loc = "Eastwood"
    print("You must attend",loc,"for your vaccine")
    # Checking if the person enrolled for the vaccine
    if trial == "Yes":
        print("You are enrolled in the trial to recieve Super \n Vaccine",select)
    # Converting the age to a int and checking within the range
    age = int(age)
    vaccine = ""
    if age < 50 and age > 11:
        vaccine = "MRNA"
    elif age > 49:
        vaccine = "ADENO"
    #print(f_name,", you will recieve the",vaccine,"vaccine")
    aux = input("If you have finished entering people\'s details type \'END\', otherwise press RETURN: ")


#question b
List = [4,5,9,8,10,17,99,77]
count = 0
#counts how many digits in a list
for i in List:
    count += 1
#Checks if the digit is odd or even in order to give the right median
if count %2==0:
    fi = count /2
    fi2 = fi + 1
    median = (List[int(fi)] + List[int(fi2)]) /2
elif count %2!=0:
    median = List[int(count//2)]
print(median)    