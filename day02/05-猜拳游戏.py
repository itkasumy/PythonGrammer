import random

player = int(input("请出拳(剪刀[0]、石头[1]、布[2]):"))

computer = random.randint(0, 2)
print("电脑出拳:%d"%computer)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You Win!!!")
elif player == computer:
    print("平局")
else:
    print("You Lost...")

print("over...")
