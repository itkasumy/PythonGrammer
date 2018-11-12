try:
    # x = 1 / 0
    f = open('a.txt')
    print('======')
except ZeroDivisionError:
    print('分母不能为零...')
except FileNotFoundError:
    print('文件不存在...')
except:
    print('捕获到异常,可以进行功能修正...')

print('程序异常...')
