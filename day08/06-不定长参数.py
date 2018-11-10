def saveInfo(mgr, *stu):
    print(mgr, stu)


saveInfo('ksm', '张三', '李四', '王五')


def saveInf(mgr, *stu, **stud):
    print(mgr, stu, stud)


saveInf('ksm', 'zhangsan', 'lisi', 'wangwu', ceo='chenqi', coo='limi')
