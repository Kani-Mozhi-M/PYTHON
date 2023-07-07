a=200
b=33
if a>b:
    print("a is greater")
elif a==b:
    print("both are equal")
else:
    print("b is greater")

name1 = "Kanimozhi"
find = input("enter your name")

#casefold() - changes to lowecase
if find in name1.casefold():
    print("string found")
else:
    print("not found")
