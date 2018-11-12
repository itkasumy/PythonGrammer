# command = input('请输入 hello 或者 hi')
#
# if command == 'hello':
#     print('你好啊,美女')
# elif command == 'hi':
#     print('你好啊,女神')

import sys

# print(sys.argv)
command = sys.argv[1]
if command == 'hello':
    print('你好啊,美女')
elif command == 'hi':
    print('你好啊,女神')
