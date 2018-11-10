import os

target = input("请输入要处理的文件夹:")

fileList = os.listdir(target)

# for file in fileList:
#     os.rename(target + '/' + file,target + '/ksm-' + file)

os.chdir(target)
for file in fileList:
    os.rename(file, 'ksm-' + file)
