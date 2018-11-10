# 猜拳游戏
import random

while True:
    # 玩家出拳
    player = int(input("请出拳(剪刀[0]、石头[1]、布[2]、退出[3]):"))

    if not player == 1 or player == 1 or player == 2 or player == 3:
        print("请输入可用的数字！！！")
        continue

    if player == 3:
        break

    # 电脑出拳
    computer = random.randint(0, 2)
    print(computer)

    # 比较结果并打印
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("You Win!")
    elif player == computer:
        print("平局，不服再战...")
    else:
        print("You Lost! 还敢再战?")

print("over...")
