#Question 1:
#according to PEMDAS () ** * / % + -
#a. 10*(90+2)-5= 10*92-5 = 920 -5 = 915
#b. 10*90+2-5= 900+2-5= 902-5= 897
#c. 10*90+(2-5)= 10*90+(-3)= 10*90-3= 900-3= 897
#d. 10.0*(90+2)-5= 10.0*92-5= 920.0-5= 915.0
#e. 120/(20+40)-(6-2)/4= 120/60-4/4= 2-1=1
#f. 5.0/2=2.5
#g. 5/2=2.5
#h. 5.0/2.0=2.5
#i. 5/2.0=2.5
#j. 678%3*(8-(9/4))=678%3*(8-2.25)= 678%3*5.75= 0*5.75= 0

print(10*(90+2)-5)
print(10*90+2-5)
print(10*90+(2-5))
print(10.0*(90+2)-5)
print(120/(20+40)-(6-2)/4)
print(5.0/2)
print(5/2)
print(5.0/2.0)
print(5/2.0)
print(678%3*(8-(9/4)))


#Question 2:
user_id = input("Enter your ID: ")
name = input("Enter your name: ")
date_of_birth = input("Enter your date of birth : ")
address = input("Enter your address: ")

print("0" + user_id)
print(name.upper())
print(date_of_birth.replace('-', '/'))
print(address.lower().strip())


#Question 3:
number = input("enter a number: ")
print(number,"has",len(number),"digits" )


#Question 4:
grade = int(input("enter a numeric grade: "))
letter_grade = ""
if grade >= 97:
  letter_grade = "A+"
elif grade >= 93 and grade < 97:
  letter_grade = "A"
elif grade >= 90 and grade < 93:
  letter_grade = "A-"
elif grade >= 87 and grade < 90:
  letter_grade = "B+"
elif grade >= 83 and grade < 87:
  letter_grade = "B"
elif grade >= 80 and grade < 83:
  letter_grade = "B-"
elif grade >= 77 and grade < 80:
  letter_grade = "C+"
elif grade >= 73 and grade < 77:
  letter_grade = "C"
elif grade >= 70 and grade < 73:
  letter_grade = "C-"
elif grade >= 67 and grade < 70:
  letter_grade = "D+"
elif grade >= 63 and grade < 67:
  letter_grade = "D"
elif grade >= 60 and grade < 63:
  letter_grade = "D-"
else:
  letter_grade = "F"
print(grade,"is equivalent to a",letter_grade,".")


#Question 5:
nmbr = int(input("enter a number n :"))
for i in range(1, nmbr + 1):
  print("*" * i)
for i in range(nmbr -1, -1, -1):
  print("*" * i)


#Question 6:
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

while number2 < number1:
    print("ERROR: Second number is smaller than the first number")
    number2 = int(input("Enter the second number: "))


even_numbers = []


for i in range(number1, number2 + 1):
    if i % 2 == 0:
        even_numbers.append(i)

result = ', '.join(map(str, even_numbers)) + '.' # to get the desired output format we transform the elements in the list to a string and join them with a "," and end with a "."
print(result)