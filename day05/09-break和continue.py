i = 10
while i > 0:
    print("还要继续刷吗？")
    if i == 6:
        print("不用刷了...")
        # break
        i -= 1
        continue
    print("正在刷倒数第 %d 个碟子..." % i)
    i -= 1

print("over...")
