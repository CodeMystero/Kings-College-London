

d = list(range(554))
data = []
for i in range(len(d)):
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\databyframe\data%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for i in range(len(lines)):
        L.append(lines[i].split('\n')[0])

    data.append(L)


print len(data)
print len(data[0])

interv = []
for i in range(0,8472):
    if i %20 == 0:
        interv.append(1)
    if i %20 !=0:
        interv.append(0)


print len(interv)
data_reduced = []
for i in range(len(data)):
    pem = []
    for j in range(len(data[i])):
        if interv[j] == 1:
            pem.append(data[i][j])
    data_reduced.append(pem)


print len(data_reduced)
print len(data_reduced[0])


for i in range(len(data_reduced)):
    print i
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\dataframebyevery15_reduced\data%s.txt"%i,"w")
    for j in range(len(data_reduced[i])):
        a = str(data_reduced[i][j])
        a = a.strip("v ")
        f.write(a)
        f.write("\n")
f.close()
