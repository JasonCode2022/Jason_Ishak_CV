for x in range(1,13):
    print(x, end=" * ")
print("\b"*3)



for x in range(8):
    print(" * ", end="+")



po_av=0
for n in range(10):
    g = int(input(f"enter {n+1} grade: "))
    if g>=0:
        po_av= po_av+g
print("the po av is: ",po_av)



s=0
for i in range(6):
    g = int(input(f"enter # {i+1}: "))
    if g%2!=0 and g>=0:
        s=s+g
print("number of odd and pos # is: ",s)


s=0
for i in range(6):
    g = int(input(f"enter your {i+1} number: "))
    if g%4 == 0:
        s=s+1
print("perc is: ",(s*100/6))



so=0
se=0
no=0
ne=0
for i in range(10):
    g = int(input(f"enter your {i+1} #: "))
    if g%2 ==0:
        se=se+g
        ne=ne+1
        ave=se/ne
    else:
        so=so+g
        no=no+1
        avo=so/no
ne=10-no
if ne==0:
    ave=0
else:
    ave=se/ne
if no==0:
    avo=0
else:
    avo=so/no

dif=avo-ave
print(f"the dif between avrages is: {dif:.0f}")




g=int(input("enter range: "))
for x in range(g):
    print(2**x,end=(" "))



g=int(input("enter range: "))
for x in range(1,g+1):
    print((2**x)-1,end=(" "))



g=int(input("enter range: "))
s=100
for x in range(g):
    print(s,end=" ")
    if x%2==0:
        s=s-2
    else:
        s=s-3


a=b=1
g=int(input("enter range: "))
print(a,b,end=" ")
for x in range(g):
    c=a+b
    print(c,end=" ")
    a=b
    b=c



g=int(input("enter range: "))
x=2
for y in range(g):
    print(x,end=" ")
    if (y+1)%5==0:
        print()
    x=x+3


s=0
i=0
while True:
    g = int(input(f"enter your {i+1} number: "))
    i+=1
    if g == -99:
        break
    if 10<=g<=55:
        s=s+g
print(s)





for x in range(4):
    for y in range(4):
        print("*",end="")
    print()

# method 2
for x in range(4):
    print("*"*4)



n = int(input("etner number of lines: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end = " ")
    print()



n = int(input("etner number of lines: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end = " ")
    print()





n = int(input("etner number of lines: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()




n = int(input("etner number of lines: "))
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()




n = int(input("etner number of lines: "))
for i in range(1,n+1):
    if i%2==1:
        print("+"*i)
    else:
        print("*"*i)



n = int(input("etner number of lines: "))
for i in range(n):
    for j in range(n):
        if j==i:
            print("+",end=" ")
        else:
            print("*",end=" ")
    print()



n = int(input("etner number of lines: "))
for i in range(n):
    for j in range(n):
        if j == i or j + i == n-1:
            print("+",end=" ")
        else:
            print("*",end=" ")
    print()





n = int(input("etner number of lines: "))
for i in range(n,0,-1):
        print("*"*i)




n = int(input("etner number of lines: "))
for i in range(1, n + 1):
    print("  " * (n-i), end="")
    print("* " * i)




n = int(input("etner number of lines: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()




n = int(input("etner number of lines: "))
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    print(" *"*(2*i-1))




n = int(input("etner number of lines: "))
for i in range(1, n + 1):
    print("  " * (n-i), end="")
    for j in range(i, 2 * i):
        print(j, end=" ")
    for k in range(j-1, i - 1, -1):
        print(k, end=" ")
    print()














