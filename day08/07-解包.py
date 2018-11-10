def saveInf(mgr, *stu, **stud):
    print(mgr, stu, stud)


stu = ['zhaoliu', 'yemi']
leader = {'banzhang': 'xunyu', 'genaral': 'caoren'}
saveInf('ksm', 'zhangsan', 'lisi', 'wangwu', *stu, ceo='chenqi', coo='limi', **leader)
