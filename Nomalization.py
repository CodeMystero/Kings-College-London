
d = list(range(424))
data = []
for i in range(len(d)):
    print i
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\PCA1D_reduced\sensor%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for j in range(len(lines)):
        L.append(lines[j].split('\n')[0])

    data.append(L)

data_float =[]
for i in range(len(data)):
    per = []
    for j in range(len(data[i])):
        a = float(data[i][j])
        per.append(a)
    data_float.append(per)

nomalized_sensors = []

for i in range(len(data_float)):
    first_value = data_float[i][0]
    pem = []
    for j in range(len(data_float[i])):
        a = (data_float[i][j]-first_value)
        pem.append(a)
    nomalized_sensors.append(pem)


for i in range(len(nomalized_sensors)):
    print i
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\Nomalizedvalues\sensor%s.txt"%d[i],"w")
    for k in range(len(nomalized_sensors[i])):
        a = str(nomalized_sensors[i][k])
        a = a.strip("[")
        a = a.strip("]")
        a = a.replace(',','')
        f.write(a)
        f.write("\n")
f.close()


