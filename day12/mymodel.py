__all__ = ['test1']

def test1():
    print('mymodel 的 test1 执行了...')


def add(a, b):
    return a + b


# print(__name__)
if __name__ == '__main__':
    print('开始测试程序的稳定性')
    test1()
    print('测试结束')