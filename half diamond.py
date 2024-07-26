def diamond(num):
    for i in range(num):  
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(num):
        for j in range(num-1-i):
            print("*",end="")
        print()
diamond(5)

                 
