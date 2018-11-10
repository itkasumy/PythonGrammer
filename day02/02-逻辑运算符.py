car = 3
home = 1
love = 0

# 只要不爱她的闺女就可以结婚
if not love == 1:
    print("可以结婚")
else:
    print("不能结婚...")

# 丈母娘要求，必须有至少3辆车并且至少有2套房，或者只要爱她的闺女，才能结婚
if (car >= 3 and home >= 2) or love == 1:
    print("可以结婚...")
else:
    print("不能结婚...")

# 丈母娘要求，必须有至少3辆车，或者至少有2套房，或者只要爱她的闺女，才能结婚
if car >= 3 or home >= 3 or love == 1:
    print("可以结婚...")
else:
    print("不能结婚...")

# 丈母娘要求，必须有至少3辆车，并且至少有2套房，并且要爱她的闺女，才能结婚
if car >= 3 and home >= 2 and love == 1:
    print("可以结婚...")
else:
    print("不能结婚...")

print("程序结束...")
