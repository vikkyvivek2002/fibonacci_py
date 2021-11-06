x = int(input("enter a number"))
a=0
b=1
temp =a+b
print(a)
print(b)
for i in range(x-2):
    print(a+b)
    a = b
    b = temp
    temp = a+b
