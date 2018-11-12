try:
    # x = 1 / 0
    # f = open('a.txt')
    print('======')
except Exception as exp:
    print('发生了一个异常...', exp)
else:
    print('如果没有发生异常else执行')
finally:
    print('不管有没有异常,最终都会执行fanally的代码')

print('程序异常...')
