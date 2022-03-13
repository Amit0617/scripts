f1 = open('ExportSQL1.sql','r')
lines = f1.readlines()
i = 0;
for line in lines:
    f1 = open('ExportSQL1.sql','a+')
    addcount = lines[i].replace('categoryId=', 'categoryId={}'.format(i))
    f1.truncate()
    f1.write(addcount)
    f1.close()
    i+=1
