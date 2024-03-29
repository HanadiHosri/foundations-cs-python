def displayMenu(): #O(1)
    print("1. Singly Linked List\n" + "2. Check if Palindrome\n" + "3. Priority Queue\n" +
        "4. Evaluate an Infix Expression\n" +"5. Graph\n" + "6. Exit")
    
def displayMenu1(): #O(1)
    print("a. Add Node\n" + "b. Display Nodes\n" + "c. Search for & Delete Node\n" + "d. Return to main menu")

def displayMenu3(): #O(1)
    print("a. Add a student\n" + "b. Interview a student\n" + "c. Return to main menu")

def displayMenu5(): #O(1)
    print("a. Add vertex\n" + "b. Add edge\n" + "c. Remove vertex\n" + "d. Remove edge\n" + "e. Display vertices witha degree of X or more\n" + "f. Return to main menu")

class Node:
    def __init__(self, info): #O(1)
       self.info = info
       self.next = None

class LinkedList:
    def __init__(self): #O(1)
       self.head = None
    
    def addNode(self,node): #O(N), where N is the number of nodes in the LL
        if self.head == None: #if the list is empty, simply make the new node the head
            self.head = node
        else:
            temp = self.head
            while temp.next != None: #we do this to reach the last element(which is pointing to None)
                temp = temp.next
            temp.next = node
            node.next = None
    
    def displayNodes(self): #O(N), where N is the number of nodes in the LL
        current = self.head
        while current != None:
            print(current.info , end=" -> ")
            current = current.next
        print("None")

    def removeNode(self, value): #O(N), where N is the number of nodes in the LL
        current = self.head
        if current == None:
            print("your list is empty, cant delete from an empty linked list")
        elif current.info == value: #if the first node is the one to be removed
            self.head = current.next
            current.next = None
        else:
            prev = current #we set previous to be the head, and current to be the next of head (the second element)
            current = current.next
            while current != None:
                if current.info == value:
                    prev.next = current.next #we are unlinking the node from the linked list by setting the next of its previous node to the next of this node
                else:
                    prev = current
                current = current.next

def checkPalindrome(str): #O(N), where N is the number of characters in str
    s = list(str)
    queue = []
    stack = []
    for x in s: #O(N), where N is the number of characters in str
        queue.append(x) #O(1)
        stack.append(x)
    while queue != [] and stack != []:
        if queue.pop(0) != stack.pop(): #dequeue in a list is the same as popping the first element, .pop() has O(1)
            return "the string is not a palindrome"
    return "the string is a palindrome"

class Student:
    def __init__(self, name, midterm_grade, final_grade, good_attitude): #O(1)
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
        
class PriorityQueue:
    def __init__(self): #O(1)
        self.head = None
        self.size = 0
        
    def displayNodes(self): #O(N), N being the number of nodes in pq
        current = self.head
        while current != None:
            print(current.info.name)
            current = current.next

    def enqueue(self, student): #O(N), N being the number of nodes in pq
        node = Node(student)
        if self.size == 0:
            self.head = node
            self.size += 1
        else :
            if node.info.good_attitude == True:
                if node.info.final_grade >= self.head.info.final_grade:
                    if node.info.midterm_grade >= self.head.info.midterm_grade:
                        node.next = self.head
                        self.head = node
                        self.size += 1
                    else:
                        current = self.head
                        previous = current
                        while current != None and current.info.good_attitude ==True and current.info.midterm_grade > node.info.midterm_grade :
                            previous =  current
                            current = current.next
                        previous.next = node
                        node.next = current
                        self.size += 1
                else:
                    current = self.head
                    previous = current
                    while current != None and current.info.good_attitude ==True and current.info.final_grade > node.info.final_grade:
                        previous =  current
                        current = current.next
                    previous.next = node
                    node.next = current
                    self.size += 1
            else:
                current = self.head
                previous = current
                while current != None:
                    previous =  current
                    current = current.next
                previous.next = node
                node.next = current
                self.size += 1

    def dequeue(self): #O(1)
        head = self.head
        if self.size == 0:
            print("Your Queue is Empty! Enqueue first.")
        elif self.size == 1:
            print("you need to interview :" , head.info.name)
            self.head = None
            self.size -= 1
        else:
            print("you need to interview :" , head.info.name)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1

# Code from chatgpt
# Function to check precedence of operators 
def precedence(operator): #O(1)
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

# Function to perform arithmetic operations
def applyOperator(operand1, operand2, operator): #O(1)
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero")
        return operand1 / operand2

# Function to evaluate the infix expression using stacks
def evaluateInfix(expression): #O(N^2), N being the number of characters in expression
    numbers_stack = []
    operators_stack = []

    for char in expression:
        if char.isdigit():
            numbers_stack.append(int(char))
        elif char == '(':
            operators_stack.append(char)
        elif char == ')':
            while operators_stack[-1] != '(':
                operator = operators_stack.pop()
                operand2 = numbers_stack.pop()
                operand1 = numbers_stack.pop()
                result = applyOperator(operand1, operand2, operator)
                numbers_stack.append(result)
            operators_stack.pop()  # Discard the '('
        else:
            while operators_stack and precedence(operators_stack[-1]) >= precedence(char):
                operator = operators_stack.pop()
                operand2 = numbers_stack.pop()
                operand1 = numbers_stack.pop()
                result = applyOperator(operand1, operand2, operator)
                numbers_stack.append(result)
            operators_stack.append(char)
    
    while operators_stack:
        operator = operators_stack.pop()
        operand2 = numbers_stack.pop()
        operand1 = numbers_stack.pop()
        result = applyOperator(operand1, operand2, operator)
        numbers_stack.append(result)

    return numbers_stack[0]

class Graph:
    def __init__(self,num_vertices): #O(1)
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def addVertex(self): #O(N), where N is the number of vertices
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)

    def displayGraph(self): #O(N), where N is the number of vertices
        if len(self.adj_matrix) == 0:
            print("Graph is empty!")
            return
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))
        
    def addEdge(self,v1,v2): #O(1)
        if 0 <= v1 < self.num_vertices and 0 <= v2 <self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
        elif ((v1 < 0 or v1>= self.num_vertices) and (v2 < 0 or v2 >= self.num_vertices)):
            print("Invalid vertices", v1, "and", v2, "\n")
        elif (v1 < 0 or v1 >= self.num_vertices):
            print("Invalid vertex", v1, "\n")
        else:
            print("Invalid vertex", v2, "\n")

    def removeVertex(self,v): #O(N), where N is the number of vertices
        matrix = []
        matrix1 = []
        if v >= self.num_vertices: #if the vertex does not exist
            return "there is no vertex number", v
        else:
            for i in range(self.num_vertices):
                self.adj_matrix[v][i] = 0
                self.adj_matrix[i][v] = 0 #deleting all the edges connected to this vertex
            for row in self.adj_matrix:
                if row != self.adj_matrix[v]: #introducing matrix which has all rows of adj_matrix except the row of the vertice we want to delete
                    matrix.append(row)
            for row in matrix:
                row1 = row[:v] + row[v+1:] #introducing matrix1 which has all columns of matrix except the column of the vertice we want to delete
                matrix1.append(row1)
            self.adj_matrix = matrix1
            self.num_vertices -= 1
    
    def removeEdge(self, v1, v2): #O(1)
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def displayVerticesDegree(self,degree): #O(N^2) where N  is the number of vertices
        v = 0 #to see at which vertex we are
        for row in self.adj_matrix:
            v += 1
            s = 0 #to find the degree of a vertex, we do the sum of the elements in the corresponding row of our AM
            for i in row:
                s = s + i
            if s >= degree:
                print("vertex", v)


def main():
    ll = LinkedList()
    pq = PriorityQueue()
    graph =Graph(0)
    name = input("enter your name :")
    print("Hello, Welcome!!", name)
    choice = 0
    limit = 0
    while choice != 6 and limit < 4:
        displayMenu()
        choice = int(input("enter your choice :"))
        if choice == 1:
            limit = 0
            choice1 = ""
            while choice1 != "d":
                displayMenu1()
                choice1 = input("enter your choice :")
                if choice1 == "a":
                    n = eval(input("enter a numerical value n to add to the linked list :"))
                    new_node = Node(n)
                    ll.addNode(new_node)
                elif choice1 == "b":
                    ll.displayNodes()
                elif choice1 == "c":
                    n = eval(input("enter a value to search for in the linked list, then delete all nodes with that value :"))
                    ll.removeNode(n)
        elif choice == 2:
            limit = 0
            str = input("enter a string to check if it is a palindrome :")
            print(checkPalindrome(str))
        elif choice == 3:
            limit = 0
            choice3 = ""
            while choice3 != "c":
                displayMenu3()
                choice3 = input("enter your choice :")
                if choice3 == "a":
                    name = input("enter a student name :")
                    midterm_grade = int(input("enter their midterm grade :"))
                    final_grade = int(input("enter their final grade :"))
                    attitude = input("enter True if the student has good attitude and False if they dont :")
                    if attitude == "True":
                        good_attitude = True
                    if attitude == "False":
                        good_attitude = False
                    student = Student(name,midterm_grade,final_grade,good_attitude)
                    pq.enqueue(student)
                    pq.displayNodes()
                elif choice3 == "b":
                    pq.dequeue()
                    pq.displayNodes()
        elif choice == 4:
            limit = 0
            infix_expression = input("Enter an infix expression using +, -, *, / operators and parenthesis: ")
            print("the result is ", evaluateInfix(infix_expression))
        elif choice == 5:
            limit = 0
            choice5 = ""
            while choice5 != "f":
                displayMenu5()
                choice5 = input("enter your choice :")
                if choice5 == "a":
                    graph.addVertex()
                    graph.displayGraph()
                elif choice5 == "b":
                    vertex1 = int(input("enter the number of the first vertex to add an edge between it and the second vertex : ")) -1
                    vertex2 = int(input("enter the number of the the second vertex :")) -1
                    graph.addEdge(vertex1,vertex2)
                    graph.displayGraph()
                elif choice5 == "c":
                    vertex = int(input("enter the number of a vertex to remove it from the graph :")) -1
                    graph.removeVertex(vertex)
                    graph.displayGraph()
                elif choice5 =="d":
                    v1 = int(input("enter the number of the first vertex to remove an edge between it and the second vertex : ")) -1
                    v2 = int(input("enter the number of the the second vertex :")) -1
                    graph.removeEdge(v1,v2)
                    graph.displayGraph()
                elif choice5 =="e":
                    n = int(input("enter a numerical value n to display all vertices with a degree of n or more :"))
                    graph.displayVerticesDegree(n)
        elif choice != 6:
            print("Invalid input\n")
            limit += 1
            print("You have reached", limit, "/4 trys\n")
    print("Goodbye! Have a nice day !")
main()