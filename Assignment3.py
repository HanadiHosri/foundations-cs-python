name = input("enter your name :")
print("Welcome!!", name)
print("1. Add Matrices\n" + "2. Check Rotation\n" + "3. Invert Dictionary\n" +
        "4. Convert Matrix to Dictionary\n" +"5. Check Palindrome\n" +
         "6. Search for an Element & Merge Sort\n" + "7. Exit")

def addMatrices(rows,cols):
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix1 = []
    
    for i in range(rows):
        row1 = []
        print("Enter elements of matrix 1 at row " , i)
        for j in range(cols): #O(N)
            print("at column " , j)
            element = int(input("Enter element "))
            row1.append(element)
        matrix1.append(row1)

    

    