for i in range(1,5,1):
    if(i==1 or i==4):
        for j in range(1,5,1):
            print("*",end=" ")
        print("")
    else:
        for j in range(1,5,1):
            if (j==1 or j==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")



def hollow_square_star_pattern(n):
    for i in range(n):
        if i==0 or i==n-1:
            print('* '*n)
        else:
            print('* '+'  '*(n-2)+'*')
hollow_square_star_pattern(4) 
print("/n")           
