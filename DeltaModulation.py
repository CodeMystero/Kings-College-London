

d = list(range(424))
data = []
for i in range(len(d)):
    print i
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\Nomalizedvalues\sensor%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for j in range(len(lines)):
        L.append(lines[j].split('\n')[0])

    data.append(L)

data_float =[]
for i in range(len(data)):
    pem = []
    for j in range(len(data[i])):
        a = float(data[i][j])
        pem.append(a)
    data_float.append(pem)

data_modulated = []
for i in range(len(data_float)):
    pem = []
    for j in range(len(data_float[i])-1):
        if data_float[i][j+1] >= data_float[i][j]:
            pem.append(1)
        if data_float[i][j+1] < data_float[i][j]:
            pem.append(0)
    data_modulated.append(pem)

for i in range(len(data_modulated)):
    print i
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\DeltaModulated_reducedsensors\sensor%s.txt"%d[i],"w")
    for k in range(len(data_modulated[i])):
        a = str(data_modulated[i][k])
        a = a.strip("[")
        a = a.strip("]")
        a = a.replace(',','')
        f.write(a)
        f.write("\n")
f.close()
