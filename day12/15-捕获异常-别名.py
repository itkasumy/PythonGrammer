try:
    # x = 1 / 0
    f = open('a.txt')
    print('======')
except (ZeroDivisionError, FileNotFoundError) as exp:
    print('文件不存在或者分母为零...', exp)
# except ZeroDivisionError as exp:
#     print('分母不能为零...', exp)
except:
    print('捕获到异常,可以进行功能修正...')

print('程序异常...')
