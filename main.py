#password generator
import random

level =input("plese eneter the level of the password simple or diffcult:")
leters=input("please enter the number of letters do you want")
symbols=input("please enter the number of symbols")
numbers=input("please the number of numericals do you want")
leter=['a','s','d','f','g','h','z','x','c','v','b','n','m']
num=[1,2,3,4,5,6,7,8,9,0]
symbl=['~','!','@','#','$','%','^','&','*','(',')','_']
arra=[]
str1=""
for i in range(int(leters)):
        choice1=random.choice(leter)
        arra.append(choice1)
for i in range(int(numbers)):
        choice1=random.choice(num)
        arra.append(choice1)
for i in range(int(symbols)):
        choice1=random.choice(symbl)
        arra.append(choice1)
if level.lower()=='simple':
    for i in range(len(arra)):
        selected=arra[i]
        str1+=str(selected)
elif level.lower()=='difficult':
    for i in range(len(arra)):
        choice1=random.choice(arra)
        str1+=str(choice1)
        arra.remove(choice1)
else:
    print("please enter the correct level")
print(str1)






