name = "kanimozhi"
print(name[0:9:2]) #output : knmzi

# reverse
print(name[9:-10:-1]) #output : ihzominak

        #01234567890123456789012345
alpha = "abcdefghijklmnopqrstuvwxyz"
        #65432109876543210987654321 (-)

print(alpha[12:15])              #output : mno
print(alpha[14:11:-1])          #output : onm
print(alpha[4:14:3])            #output : ehkn
print(alpha[0:8])               #output : abcdefgh
print(alpha[13:-23:-3])          #output : nkhe
print(alpha[-1:5:-1])            #output : zyxwvutsrqponmlkjihg
print(alpha[:20])                #output : abcdefghijklmnopqrst

print(len(alpha))                #output : 26
print(len(alpha[:2]))             #output : 2

#string replacement

weight=60
print("I am raji my weight is {}".format(weight)) #I am raji my weight is 60

print("I BOUGHT {0} AND {1} . WHAT YOU LIKE TO HAVE? ".format("APPLE","ORANGES"))
#I BOUGHT APPLE AND ORANGES . WHAT YOU LIKE TO HAVE?

print()
for i in range(4, 6):
    print("no.{0} square is{1} and cube is{2} ".format(i, i ** 2, i ** 3))

for i in range(4, 6):
    print("no.{0} square is {1:<2} and cube is {2:^4} ".format(i, i ** 2, i ** 3))

name1 = "kanimozhi"
print([str(val) for val in name1])  #['k', 'a', 'n', 'i', 'm', 'o', 'z', 'h', 'i']

print()

#multiplication table
for i in range(1,4):
    for j in range(1,11):
        print("{0} * {1} = {2}".format(i,j,i*j))
    print()

weight=50
print(f"my wght is {weight}")
