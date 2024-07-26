def diamond(num):
    for i in range(num):
        for j in range(num-i-1):
            print(" ",end="")
        for j in range(i*2+1):
            print("*",end="")
        print()
    for i in range(1,num):
        for j in range(i):
            print(" ",end="")
        for j in range((num-i)*2-1):
            print("*",end="")
        print()
diamond(5)
print("\n")    
def half_diamond(num):
 for i in range(num):
        for j in range(i+1):
            print("*",end="")
        for j in range():
            print("*")
        print()      
half_diamond(5)
                 
