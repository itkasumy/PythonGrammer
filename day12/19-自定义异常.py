class MyError(Exception):

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return '年龄不能小于0,您输入的是 %d' % self.age

try:
    age = int(input('请输入年龄:'))
    if age < 0:
        raise MyError(age)
except MyError as exp:
    print('捕获到一个异常:', exp)


print('over...')
