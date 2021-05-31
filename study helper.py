from googlesearch import search
import time
import random
import webbrowser
import urllib.request
from bs4 import BeautifulSoup

while True:
    print("STUDY HELPER")
    print("")
    tool = input("1. Google Search, 2. Calculator, 3. definition finder, 4. Exit: ")

    if tool == "1":
        query = input("what do you want to search: ")
        #  iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % query)
    

    if tool == "2":
        def add(x, y):
            return x + y
        math = input("1. add, 2. subtract, 3. multiply, 4 divide: ")
        if math == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))

        elif math == '2':
            def subtract(x, y):
                return x - y
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif math == '3':
            def multiply(x, y):
                return x * y
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif math == '4':
            def divide(x, y):
                return x / y
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))

    if tool == "3":
        word = input('Enter the word of which you want to find the meaning: ')

        url = "https://www.vocabulary.com/dictionary/" + word + ""
        htmlfile = urllib.request.urlopen(url)
        soup = BeautifulSoup(htmlfile, 'lxml')
        soup1 = soup.find(class_="short")

        # If certain word's meaning is not found
        try:
            soup1 = soup1.get_text()
        except AttributeError:
            print('Cannot find such word! Check spelling.')
            

        # Print short meaning
        print ('-' * 25 + '->',word,"<-" + "-" * 25)
        print ("SHORT MEANING: ",soup1)
        print ('-' * 65)

        # Print long meaning
        soup2 = soup.find(class_="long")
        soup2 = soup2.get_text()

        print ('-' * 65)

        # Print instances like Synonyms, Antonyms, etc.
        soup3 = soup.find(class_="instances")
        txt = soup3.get_text()
        txt1 = txt.rstrip()

        print (' '.join(txt1.split()))

    if tool == "4":
        sure = input
        print("goodbye")
        time.sleep(5)
        quit()
        