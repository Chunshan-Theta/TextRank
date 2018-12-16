import csv
f = open("dic.csv","r")
w = csv.reader(f)
f2 = open("dic.txt","a")
for i in w:
    print i[1]
    f2.write(i[1]+'\n')
