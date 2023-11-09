def displayMenu():
   print("1. Open Tab\n" + "2. Close Tab\n" + "3. Switch Tab\n" + "4. Display All Tabs\n" +"5. Open Nested Tab\n" + "6. Clear All Tabs\n"+ "7. Save Tabs\n" + "8. Import Tabs\n" + "9. Exit")

def openTab():
   title = input("enter title of the website :")
   url = input("enter URL of the website :")
   tab = {}
   tab[url]=[title]