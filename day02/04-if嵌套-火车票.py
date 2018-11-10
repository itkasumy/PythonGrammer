danger = 0
ticket = 0

if danger == 1:
    print("没有危险品,可以进站...")
    if ticket == 1:
        print("有票，可以上车")
    else:
        print("没票，不可以上车...")
else:
    print("有危险品，不可以进站")

print("over...")
