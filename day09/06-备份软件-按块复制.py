fromName = input("请输入要备份的文件名:")
idx = fromName.rfind('.')
toName = fromName[:idx] + '[附件]' + fromName[idx:]

fFrom = open(fromName, 'r')
fTo = open(toName, 'w')

while True:
    content = fFrom.read(1024 * 8)

    if len(content) == 0:
        break

    fTo.write(content)

fFrom.close()
fTo.close()
