#Question 1:
def reverseConc(string, integer):
  if integer == 0: 
    return ""
  str1 = ""
  for i in range(len(string)-1,-1,-1):
    str1 += string[i]
  return str1 * integer

string = input("enter a string s :")
integer = int(input("enter an integer i :"))
while integer < 0 :
  integer = int(input("ERROR, enter a POSITIVE integer :"))
print(reverseConc(string,integer))


#Question 2:
def arrangeStr(string):
  string = string.replace(" ","")
  str1 = ""
  str2 = ""
  for i in range(len(string)):
    if string[i].isupper():
      str1 += string[i]
    else:
      str2 += string[i]
  return str1 + str2

string = input("enter a string S :")
print(arrangeStr(string))


#Question 3:
def checkReordering(str1, str2):
  str3 =""
  if len(str1) == len(str2):#here we can work with the 2 strings since they have the same length
    for i in range(len(str1)): # we use this line to check each element in str1
      for j in range (len(str2)): #same thing for str2
        if str1[i] == str2[j]: #we check in order if any character in str2 is equal to a character in str1() 
          str3 += str1[i] #we append str3 where we take the character from str1 if it exists in str2 too.
    return str1 == str3 #this will return True if str1=str3 and False if they arent equal
  return False #if str1 and str2 arent of the same length, str2 cant be a reodering of characters str1

str1 = input("enter the first string S1 :")
str2 = input("enter the second string S2 :")
print(checkReordering(str1, str2))


#Question 4:
def findMax(input_list):
  max_value = 0
  index = 0
  for i in range(len(input_list)):
      if input_list[i] > max_value:
          max_value = input_list[i]
          index = i
  return max_value, index

my_list = [5, 6, 3, 2, 7, 2, 0, 1, 6]
max_value, max_index = findMax(my_list)

print("The highest value in the list is", max_value, "at index", max_index)

#in case we had the max twice in the list such as [5, 6, 3, 2, 7, 2, 0, 1, 6, 7]
def findMax1(input_list):
  max_value = 0
  max_indices = []

  for i in range(len(input_list)):
      if input_list[i] > max_value:
        max_value = input_list[i]
        max_indices = [i]

      elif input_list[i] == max_value:
          max_indices.append(i)

  return max_value, max_indices

my_list = [5, 6, 3, 2, 7, 2, 0, 1, 6, 7]
max_value, max_indices = findMax1(my_list)

for i in range(len(max_indices)):
  print("The highest value in the list is", max_value, "at index", max_indices[i])



#Question 5:
def sumDigits(number):
  if number < 10:
    return number
  return number%10 + sumDigits(number//10)

number = int(input("enter a number n: "))
while number < 0:
  number = int(input("enter a positive number n: "))
print(sumDigits(number))


#Question 6:
def removeConsecutiveDuplicates(str):
  # Base case: If the string is empty or has only one character, return it as is.
  if len(str) < 2:
      return str

  # If the current character is the same as the next character, skip the current character.
  if str[0] == str[1]:
      return removeConsecutiveDuplicates(str[1:])
  else:
      # If the current character is different from the next character, keep it and process the rest.
      return str[0] + removeConsecutiveDuplicates(str[1:])


str1 = input("enter a string s :")
print(removeConsecutiveDuplicates(str1))


#Question 7:
def reverseDigits(number):
  if number < 10:
    return number
  exp = 0
  nbr = number
  while nbr != 0:
    exp += 1
    nbr = nbr//10

  return (number%10)*(10**(exp-1)) + reverseDigits(number//10)

num = int(input("enter a number n :"))
print(reverseDigits(num))