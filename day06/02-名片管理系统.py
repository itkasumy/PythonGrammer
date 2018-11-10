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
    command = int(input("请输入要操作的命令数字:"))
    # print("用户输入的指令是:%s" % command)
    if command == 1:
        # 添加
        # 让用户输入要添加的名字
        newName = input("请输入要添加的名字:")
        # 保存名字
        cardList.append(newName)
        print("列表:%s" % cardList)

    elif command == 2:
        # 删除
        # 输入要删除的名字
        deleteName = input("请输入要删除的名字:")
        if deleteName in cardList:
            # 从列表中删除
            cardList.remove(deleteName)
        else:
            print("要删除的名字不存在...")

    elif command == 3:
        # 修改
        # 获取两个名字
        oldName = input("请输入要修改的名字")
        newName = input("请输入新的名字")
        # 查找旧名字查找下标
        if oldName in cardList:
            idx = cardList.index(oldName)
            # 使用新名字替换旧名字
            cardList[idx] = newName
        else:
            print("没有这个名字，无法修改...")

    elif command == 4:
        # 查看
        # 让用户输入要查找的名字
        findName = input("请输入您要查找的名字:")
        # 判断名字是否在列表里
        if findName in cardList:
            print("找到了...")
        else:
            print("没找到...")

    elif command == 5:
        # 查看所有名字
        for card in cardList:
            print(card)

    elif command == 0:
        # 退出系统
        break

    else:
        # 错误
        print("命令错误，请输入可用的数字。")

print("over...")
