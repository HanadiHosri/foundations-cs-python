name = input("enter your name :")
print("Welcome!!", name)
print("1. Add Matrices\n" + "2. Check Rotation\n" + "3. Invert Dictionary\n" +
        "4. Convert Matrix to Dictionary\n" +"5. Check Palindrome\n" +
         "6. Search for an Element & Merge Sort\n" + "7. Exit")

def addMatrices(rows,cols):
    matrix1 = []
    
    for i in range(rows):
        row1 = []
        print("Enter elements of matrix 1 at row " , i)
        for j in range(cols): #O(N)
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

    matrix3 = [[0 for j in range(cols)] for i in range(rows)] 
    for i in range(rows): 
        for j in range(cols):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrix3

def checkRotation(matrix1,matrix2):
  if len(matrix1) != len(matrix2[0]) or len(matrix1[0]) != len(matrix2): # where len(matrix1) is the number of rows and len(matrix1[0]) is the number of columns of matrix1, same for matrix2
    return "The two matrices are not rotations of each other due to different dimensions."
   #if the 2 matrices are eligible in siza to be a rotation of each other we continue  
  matrix3 = [[0 for i in range(len(matrix1))] for j in range(len(matrix1[0]))] #introducing matrix 3 as an emtpy matrix with the same size as matrix1 and then making it the rotation of matrix1
  for i in range(len(matrix1)-1):
    for j in range(len(matrix1[0])-1):
      matrix3[i][j] = matrix1[j][i]  
  if matrix2 == matrix3: #if matrix2 is equal to matrix3 which is the rotation of matrix one we return that the two matrices are rotations of each other
    return "the two matrices are rotations of each other."
  return "the two matrices are not rotations of each other."

def invertDict(dict):
  new_dict = {}  # Create an empty dictionary to store the inverted values
  new_values = []
  new_keys = []
  for key, value in dict.items():
    new_values.append(key)
    new_keys.append(value)
    #if new_keys has a duplicate inside we check for the old key and add it to a list inside new_values
  if len(new_keys) != len(set(new_keys)): #in sets we have no duplicates, so if the lengths of the original list and the set are different, that means there were duplicates.
    new_dict = dict(zip(new_keys, new_values))
    
  return new_dict
                