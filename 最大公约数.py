a = int(input( ))
b = int(input( ))
if a<=b :
    for i in range (a,0,-1):
        if a%i==0and b%i==0:
            print(i)
            import sys
            sys.exit()
else:
    for i in range (b,0,-1):
        if a%i==0 and b%i==0:
            print(i)
            import sys
            sys.exit()







