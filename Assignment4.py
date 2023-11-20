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
        elif current == Node(value): #if the first node is the one to be removed
            self.head = current.next
            current.next = None
        else:
            while current.next != None:
                if current == Node(value):
                    
                current = current.next


def main():
  ll = LinkedList()
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




main()