x = 5
if (type(x)is int):
    print("true")
else:
    print("false")

x = 5.5
if (type(x)is not float):
    print("true")
else:
    print("false")

x = 20
y = 20
if (x is y):
    print("x and y have the same identity")
else:
    print("they are not the same identity")


a = 10
b = -10
print("a>>1=",a>>1)
print("b>>1=",b>>1)
c = -1
d = 5
print("c<<1=",c<<1)
print("d<<1=",d<<1)




print("Enter the marks of the 5 subjects")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())
total = mark1+mark2+mark3+mark4+mark5
average = total/5
validrange=range(0,101)
if average not in validrange:
    print("Invalid input")
elif average in range (91,101):
    print("Your grade is A1")
elif average in range (81,91):
    print("Your grade is B1")