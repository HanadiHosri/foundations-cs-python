import requests
from bs4 import BeautifulSoup

def displayMenu():
   print("1. Open Tab\n" + "2. Close Tab\n" + "3. Switch Tab\n" + "4. Display All Tabs\n" +"5. Open Nested Tab\n" + "6. Clear All Tabs\n"+ "7. Save Tabs\n" + "8. Import Tabs\n" + "9. Exit")

def openTab(title, url):
   tab = {}
   tab[url]=[title]
   return tab

def closeTab(lst,index):
   lst.remove(lst[index])

def switchTab(url): #code from https://www.geeksforgeeks.org/python-web-scraping-tutorial/
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser') 
   return soup.prettify()

def printTabs(tab):
   for i in tab:
      print(tab[i])

def printNestedTabs(tab):
   is_parent_tab = True #since the first key is associated with the parent tab
   for i in tab:
      if is_parent_tab:
         print(tab[i])
         is_parent_tab = False #since all other keys belong to the children/nested tabs
      else :
         print("\t", end = " ")
         print(tab[i])

def openNestedTab(parent_tab):
   url = input("enter url for this nested tab :")
   title = input("enter title for this nested tab :")
   parent_tab[url] = [title]
   return parent_tab


   

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
      elif choice == 2:
         i = input("enter the index of the tab you wish to close :")
         if i == "":
            closeTab(open_tabs,len(open_tabs)-1)
         else:
            i = int(i)
            closeTab(open_tabs,i) 
      elif choice == 3:
         i = input("enter the index of the tab to display its content :")
         if i =="":
            tab = open_tabs[len(open_tabs)-1]
            for url in tab:
               u = url
            print(switchTab(u))
         else :
            i = int(i)
            tab = open_tabs[i]
            for url in tab:
               u = url
            print(switchTab(u))
      elif choice == 4:
         for tab in open_tabs:
            if len(tab) > 1:
               printNestedTabs(tab)
            else:
               printTabs(tab)
               
      elif choice == 5:
         x = int(input("enter index of the parent tab :"))
         parent_tab = open_tabs[x]
         open_tabs[x] = openNestedTab(parent_tab)
      elif choice == 6:
         open_tabs=[]
      
      


main()

