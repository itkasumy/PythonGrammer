fromName = input("请输入要备份的文件名:")
toName = "[附件]" + fromName

fFrom = open(fromName, 'r')
content = fFrom.read()
fFrom.close()

fTo = open(toName, 'w')
fTo.write(content)
fTo.close()
