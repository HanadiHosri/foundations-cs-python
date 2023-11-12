import requests
from bs4 import BeautifulSoup
import json

def displayMenu():
   print("1. Open Tab\n" + "2. Close Tab\n" + "3. Switch Tab\n" + "4. Display All Tabs\n" +"5. Open Nested Tab\n" + "6. Clear All Tabs\n"+ "7. Save Tabs\n" + "8. Import Tabs\n" + "9. Exit")

def openTab(title, url): #O(1)
   tab = {}
   tab[url]=[title]
   return tab

def closeTab(lst,index):#O(N), N being the length of the list
   lst.remove(lst[index])

def switchTab(url): #code from https://www.geeksforgeeks.org/python-web-scraping-tutorial/
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser') 
   return soup.prettify()

def printTabs(tab): #O(N), N being the number of keys  in tab
   for i in tab:
      print(tab[i])

def printNestedTabs(tab): #O(N), N being the number of keys in tab(the parent tab)
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

def saveTAbs(tabs,file_path): #code from https://www.w3schools.com/python/python_json.asp
   y = json.dumps(tabs)
   f = open(file_path, "a") #code from https://www.w3schools.com/python/ref_file_write.asp
   f.write(y)
   f.close

def importTabs(file_path): #code from https://www.w3schools.com/python/ref_file_read.asp & https://www.geeksforgeeks.org/read-json-file-using-python/
   f = open(file_path)
   data = json.load(f)
   f.close()
   return data
   

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
      elif choice == 7:
         file_path = input("enter a file path to save the current state of open tabs :")
         saveTAbs(open_tabs,file_path)
      elif choice == 8:
         file_path = input("enter a file path to load tabs from the specified file :")
         open_tabs = importTabs(file_path)
      elif choice != 9:
         print("invalid input")
   print("goodbye !")
      


main()

