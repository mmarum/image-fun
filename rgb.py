x=51
a=0
b=0
for group in range(0,36):
    if group % 6:
        pass
    else:
        AA = a*x
        a+=1
        b=0
    BB = b*51
    for c in range(0,6):
        print(AA,BB,c*x)
    b+=1