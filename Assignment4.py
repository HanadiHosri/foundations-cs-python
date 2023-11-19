def displayMenu():
    print("1. Singly Linked List\n" + "2. Check if Palindrome\n" + "3. Priority Queue\n" +
        "4. Evaluate an Infix Expression\n" +"5. Graph\n" + "6. Exit")
    
def displayMenu1():
    print("a. Add Node\n" + "b. Display Nodes\n" + "c. Search for & Delete Node\n" + "d. Return to main menu")

class Node:
    def __init__(self, info):
       self.info = info
       self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
    
    def addNode(self,value):
        new_node = Node(value)
        if self.head == None: #if the list is empty, simply make the new_node the head
            self.head = new_node
            return
        else:
            temp = self.head
            while (temp.next != None): #we do this to reach the last element(which is pointing to None)
                temp = temp.next
            temp.next = new_node
            new_node.next = None
    
    def displayNodes(self):
        current = self.head
        while current != None:
            print(current.info , end=" -> ")
            current = current.next
        print()


def main():
  name = input("enter your name :")
  print("Hello, Welcome!!", name)
  choice = 0
  while choice != 7:
    displayMenu()
    choice = int(input("enter your choice :"))
    if choice == 1:
        displayMenu1()
        choice1 = input("enter your choice :")
        ll = LinkedList()
        if choice1 == "a":
            n = eval(input("enter a numerical value n to add to the linked list :"))
            ll.addNode(n)
        if choice1 == "b":
            ll.displayNodes()


main()