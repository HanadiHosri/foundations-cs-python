def displayMenu():
    print("1. Singly Linked List\n" + "2. Check if Palindrome\n" + "3. Priority Queue\n" +
        "4. Evaluate an Infix Expression\n" +"5. Graph\n" + "6. Exit")
    
def displayMenu1():
    print("a. Add Node\n" + "b. Display Nodes\n" + "c. Search for & Delete Node\n" + "d. Return to main menu")

def displayMenu3():
    print("a. Add a student\n" + "b. Interview a student\n" + "c. Return to main menu")

class Node:
    def __init__(self, info):
       self.info = info
       self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
    
    def addNode(self,node):
        if self.head == None: #if the list is empty, simply make the new node the head
            self.head = node
        else:
            temp = self.head
            while temp.next != None: #we do this to reach the last element(which is pointing to None)
                temp = temp.next
            temp.next = node
            node.next = None
    
    def displayNodes(self):
        current = self.head
        while current != None:
            print(current.info , end=" -> ")
            current = current.next
        print("None")

    def removeNode(self, value):
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

def checkPalindrome(str):
    s = list(str)
    queue = []
    stack = []
    for x in s:
        queue.append(x)
        stack.append(x)
    while queue != [] and stack != []:
        if queue.pop(0) != stack.pop(): #dequeue in a list is the same as popping the first element
            return "the string is not a palindrome"
    return "the string is a palindrome"

class Student:
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
        
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def displayNodes(self):
        current = self.head
        while current != None:
            print(current.info.name)
            current = current.next
    def enqueue(self, student):
        node = Node(student)
        if self.size == 0:
            self.head = node
            self.size += 1
        else :
            if node.info.good_attitude == True:
                if node.info.final_grade > self.head.info.final_grade:
                    if node.info.midterm_grade > self.head.info.midterm_grade:
                        node.next = self.head
                        self.head = node
                        self.size += 1
            else:
                current = self.head
                previous = current
                while current != None and current.info.midterm_grade > node.info.midterm_grade:
                    previous =  current
                    current = current.next
                previous.next = node
                node.next = current
                self.size += 1

def main():
  ll = LinkedList()
  pq = PriorityQueue()
  name = input("enter your name :")
  print("Hello, Welcome!!", name)
  choice = 0
  while choice != 7:
    displayMenu()
    choice = int(input("enter your choice :"))
    if choice == 1:
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
        str = input("enter a string to check if it is a palindrome :")
        print(checkPalindrome(str))
    elif choice == 3: 
        choice3 = ""
        while choice3 != "c":
            displayMenu3()
            choice3 = input("enter your choice :")
            if choice3 == "a":
                name = input("enter a student name :")
                midterm_grade = int(input("enter their midterm grade :"))
                final_grade = int(input("enter their final grade :"))
                attitude = input("enter True if the student has good attitude and False if they dont :")
                good_attitude = bool(attitude)
                student = Student(name,midterm_grade,final_grade,good_attitude)
                pq.enqueue(student)
                pq.displayNodes() #remove this 




main()