# 1. 打印系统提示信息
print("="*30)
print("欢迎使用 名片管理系统 v1.0")
print("1. 添加名片")
print("2. 删除名片")
print("3. 修改名片")
print("4. 查看名片")
print("5. 查看所有名字")
print("0. 退出系统")
print("="*30)

cardList = []   # 创建列表存储用户姓

while True:
    # 2. 获取用户的操作指令
    command = int(input("请输入要操作的命令数字(0-5):"))
    if command == 1:
        # 添加
        newName = input("请输入一个新的名字:")
        newTel = input("请输入一个新的电话:")
        newAddr = input("请输入一个新的地址:")

        card = {}

        card['name'] = newName
        card['tel'] = newTel
        card['addr'] = newAddr

        cardList.append(card)
        print(cardList)

    elif command == 2:
        # 删除
        pass

    elif command == 3:
        # 修改
        oldName = input("请输入要修改的名字")
        newName = input("请输入新的名字")

        for card in cardList:
            if card['name'] == oldName:
                card['name'] = newName
                break
        else:
            print("没有找到，无法修改...")

    elif command == 4:
        # 查看
        pass

    elif command == 5:
        # 查看所有名字
        for card in cardList:
            print("="*20)
            print("姓名: %s" % card['name'])
            print("电话: %s" % card['tel'])
            print("住址: %s" % card['addr'])
            print("="*20)

    elif command == 0:
        # 退出系统
        break

    else:
        # 错误
        print("命令错误，请输入可用的数字。")

print("over...")
