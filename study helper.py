from googlesearch import search
import time
import random
import webbrowser

while True:
    print("STUDY HELPER")
    print("")
    tool = input("1. Google Search, 2. Calculator, 3. Exit: ")

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
        sure = input
        print("goodbye")
        time.sleep(5)
        quit()
        