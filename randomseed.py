import random
list1=[1,3,5,7,8,0,4,32,32]
random.seed(0)
for i in range(len(list1)):

    randomchoice=random.choice(list1)
    print(randomchoice,end=' ')
print()
for i in range(5):
    # Any number can be used in place of '0'.
    random.seed(6700)

    # Generated random number will be between 1 to 1000.
    print(random.randint(1, 1000))