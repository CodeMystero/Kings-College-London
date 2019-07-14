d = ["{0:03}".format(i) for i in range(555)]
del d[0]
data = []
for i in range(len(d)):
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\data_0000%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for i in range(len(lines)):
        L.append(lines[i].split('\n')[0])

    del L[0]
    del L[0]

    data1 = []
    for i in range(len(L)):
        if 'n' not in L[i] and 't' not in L[i] and 'f' not in L[i] and 's' not in L[i]:
            data1.append(L[i])
    data1 = data1[0:8472] ## 8472 -> Cloth
    data.append(data1)

for i in range(len(data)):
    print i
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\databyframe\data%s.txt"%i,"w")
    for j in range(len(data[i])):
        a = str(data[i][j])
        a = a.strip("v ")
        f.write(a)
        f.write("\n")
f.close()

