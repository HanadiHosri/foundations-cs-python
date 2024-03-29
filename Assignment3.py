def displayMenu():
   print("1. Add Matrices\n" + "2. Check Rotation\n" + "3. Invert Dictionary\n" +
        "4. Convert Matrix to Dictionary\n" +"5. Check Palindrome\n" +
         "6. Search for an Element & Merge Sort\n" + "7. Exit")

def addMatrices(rows,cols): #O(N^2) , N being the number of rows or cols
    matrix1 = []
    
    for i in range(rows):
        row1 = []
        print("Enter elements of matrix 1 at row " , i)
        for j in range(cols): 
            print("at column " , j)
            element = int(input("Enter element "))
            row1.append(element)
        matrix1.append(row1)

    matrix2 = []
    for i in range(rows):
        row2 = []
        print("Enter elements of matrix 2 at row " , i)
        for j in range(cols):
            print("at column " , j)
            element = int(input("Enter element "))
            row2.append(element)
        matrix2.append(row2)

    matrix3 = [[0 for j in range(cols)] for i in range(rows)]  #this is a way to introduce an empty matrix with the same dimentions as matrix1 and 2
    for i in range(rows): 
        for j in range(cols):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrix3

def checkRotation(matrix1,matrix2): #O(N^2) , N being the length of rows or columns in matrix1
  if len(matrix1) != len(matrix2[0]) or len(matrix1[0]) != len(matrix2): # where len(matrix1) is the number of rows and len(matrix1[0]) is the number of columns of matrix1, same for matrix2
    return "The two matrices are not rotations of each other due to different dimensions."
   #if the 2 matrices are eligible in size to be a rotation of each other we continue  
  matrix3 = [[0 for j in range(len(matrix1))] for i in range(len(matrix1[0]))] #introducing matrix 3 as an emtpy matrix with the rotation size of matrix1 and then we introduce the values
  for i in range(len(matrix1)-1): # i goes from 0 to the length of the rows in matrix1 -1, -1 because we start from 0
    for j in range(len(matrix1[0])-1): #j goes from 0 to the length of columns in matrix1 -1 
      matrix3[i][j] = matrix1[j][i]
      if matrix2[i][j] == matrix3 [i][j]:
         return "the two matrices are rotations of each other."  
  return "the two matrices are not rotations of each other."

def invertDict(input_dict): #O(N) , where N is the number of keys in input_dict
    inverted_dict = {}
    
    for key, value in input_dict.items():
        value = str(value)
        if value not in inverted_dict: #if the value is not in inverted_dict we add a new element to our inverted_dict where the key is the value of input_dict and the value is the key of input_dict
            inverted_dict[value] = [key]
        else: #if the value already exists in inverted_dict we append the keys (of this value) to inverted_dict at the new key (which is the old value)
            inverted_dict[value].append(key)
    return inverted_dict

def convertMatrixtoDict(matrix): #O(N) , N being the number of rows in matrix
  output_dict = {}
  values = []
  for row in range(len(matrix)):
    key = matrix[row][2]
    values = matrix[row][:2] + matrix[row][3:] #2 is exclusive , 3 is inclusive
    output_dict[key] = values
  return output_dict

def checkPalindrome(s): #O(N) , N being the length of s / 2
   if len(s) == 1: #base case, if the string is just 1 character
      return True
   if s[0] == s[-1]: #if the first and last character are the same, check the substring without them
      return checkPalindrome(s[1:-1]) #1 is inclusive, -1 exclusive
   return False #if the first and last characters are different, it's not a palindrome

def elementSearch(x,l): #O(N)
  index_lst =[]
  for i in range(len(l)):
    if l[i] == x:
        index_lst.append(i)
  return index_lst

def mergeSort(l): #code edited from https://www.youtube.com/watch?v=cVZMah9kEjI ; O(NlgN) where N is the number of elements in l 
  if len(l) > 1:
    mid = len(l)//2
    left_half = l[:mid]
    right_half = l[mid:]
    mergeSort(left_half)
    mergeSort(right_half)
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        l[k] = left_half[i]
        i += 1
      else:
        l[k] = right_half[j]
        j += 1
      k += 1
    while i < len(left_half):
       l[k] = left_half[i]
       i += 1
       k += 1
    while j < len(right_half):
       l[k] = right_half[j]
       j += 1
       k += 1
  return l

def main(): #O(n), where n is the number of times the loop iterates.(number of choices)
  name = input("enter your name :")
  print("Hello, Welcome!!", name)
  choice = 0
  while choice != 7:
    displayMenu()
    choice = int(input("enter your choice :"))
    if choice == 1:
      rows = int(input("enter number of rows :"))
      cols = int(input("enter number of columns :"))
      print(addMatrices(rows,cols))
    elif choice == 2:
      matrix1 = eval(input("Enter the first matrix as a nested list: "))
      matrix2 = eval(input("Enter the second matrix as a nested list: "))
      print(checkRotation(matrix1,matrix2))
    elif choice == 3:
      dictt = {}
      num_keys = int(input("enter number of keys :"))
      for i in range(num_keys):
        print("for key", i)
        key = input("enter a key :")
        value = input("enter a value :")
        dictt[key] = [value]
      print(invertDict(dictt))
    elif choice == 4:
      m = [["firstname1", "lastname1", "ID1", "jobtitle1", "company1"], ["firstname2","lastname2", "ID2", "jobtitle2", "company2"], ["firstname3", "lastname3", "ID3","jobtitle3", "company3"]]
      print(convertMatrixtoDict(m))
    elif choice == 5:
      str = input("enter a string s :")
      print(checkPalindrome(str))
    elif choice == 6:
      listt = [7, 5, 2, 0, 1, 2, -15, 6, -3]
      number = eval(input("Enter a number to search for: "))
      result = elementSearch(number, listt)
      if len(result) == 0:
        print("The number was not found in the list")
      else:
        print("The number was found at:", result)
      print(mergeSort(listt))
    elif choice != 7:
      print("invalid input")
  print("goodbye!")
main()
#O(N^2), Overall, the code's time complexity is determined by the most time-consuming function, which is addMatrices or checkRotation, both with O(N^2) complexity. 