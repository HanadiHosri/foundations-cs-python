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

    