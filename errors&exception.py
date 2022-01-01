# Enter your code here. Read input from STDIN. Print output to STDOUT
        #print("Error Code: invalid literal for int() with base 10: '$'")
    
for test in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        result = a // b
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
