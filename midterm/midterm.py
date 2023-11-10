def displayMenu():
   print("1. Open Tab\n" + "2. Close Tab\n" + "3. Switch Tab\n" + "4. Display All Tabs\n" +"5. Open Nested Tab\n" + "6. Clear All Tabs\n"+ "7. Save Tabs\n" + "8. Import Tabs\n" + "9. Exit")

def openTab(title, url):
   tab = {}
   tab[url]=[title]
   return tab
   

def main():
   print("Greetings !")
   choice = 0
   open_tabs = []
   while choice != 9:
      displayMenu()
      choice = int(input("enter your choice :"))
      if choice == 1:
        title = input("enter title of the website :")
        url = input("enter URL of the website :")
        open_tabs.append(openTab(title,url))
main()

