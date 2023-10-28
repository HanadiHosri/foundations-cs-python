name = input("enter your name :")
print("Welcome!!", name)
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
  if matrix2 == matrix3: #if matrix2 is equal to matrix3 which is the rotation of matrix one we return that the two matrices are rotations of each other
    return "the two matrices are rotations of each other."
  return "the two matrices are not rotations of each other."

def invertDict(input_dict): #O(N) , where N is the number of keys in input_dict
    inverted_dict = {}
    
    for key, value in input_dict.items():
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

def checkPalindrome(s):
   if len(s) == 1: #base case, if the string is just 1 character
      return True
   if s[0] == s[-1]: #if the first and last character are the same, check the substring without them
      return checkPalindrome(s[1:-1]) #1 is inclusive, -1 exclusive
   return False #if the first and last characters are different, it's not a palindrome

def elementSearchSort(x,l):
  index_lst =[]
  for i in range(len(l)):
    if list[i] == x:
        index_lst.append(i)
  return index_lst