import math
from math import pow

d = list(range(8472))
data = []
for i in range(len(d)):
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\PCA1D\data%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for i in range(len(lines)):
        L.append(lines[i].split('\n')[0])

    data.append(L)


data_float =[]
for i in range(len(data)):
    per = []
    for j in range(len(data[i])):
        per.append(float(data[i][j]))
    data_float.append(per)



##Correlation
mean_all = []
for i in range(len(data_float)):
    a = sum(data_float[i])/len(data_float[i])
    mean_all.append(a)


cor = []
for i in range(len(data_float)):
    pem = []
    for j in range(len(data_float)):
        if j>i:
            print i
            print j
            zero_mean = []
            zero_mean_x = []
            zero_mean_y = []
            for k in range(len(data_float[i])):
                a = (data_float[i][k]-mean_all[i])*(data_float[j][k]-mean_all[j])
                b = pow(data_float[i][k]-mean_all[i],2)
                c = pow(data_float[j][k]-mean_all[j],2)
                zero_mean.append(a)
                zero_mean_x.append(b)
                zero_mean_y.append(c)
            d = sum(zero_mean)/len(data_float[i])
            e = sum(zero_mean_x)/len(data_float[i])
            f = sum(zero_mean_y)/len(data_float[i])
            g = math.sqrt(e*f)
            h = d/g
            o = abs(h)
            pem.append(o)
    cor.append(pem)



    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\correlation\data%s.txt"%i,"w")
    for j in range(len(pem)):
        a = str(pem[j])
        f.write(a)
        f.write("\n")
    f.close()







