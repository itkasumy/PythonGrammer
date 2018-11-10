danger = 0
ticket = 1

if danger == 0:
    print("没有危险物品，可以进站...")
    if ticket == 1:
        print("有票，可以上车...")
    else:
        print("没票，不可以上车...")
else:
    print("有危险物品，不能进站...")

print("over...")
