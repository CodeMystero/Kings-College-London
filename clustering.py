
from operator import add

d = list(range(8472))
corr = []
for i in range(len(d)):
    print i
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\correlation\data%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for i in range(len(lines)):
        L.append(lines[i].split('\n')[0])
    corr.append(L)
##
##print len(corr)      -->8472
##print len(corr[0])   -->8471
##print len(corr[8469]) -->2
##print len(corr[8470]) -->1
##print len(corr[8471]) -->0
corr_float =[]
for i in range(len(corr)):
    per = []
    for j in range(len(corr[i])):
        a = float(corr[i][j])
        a = round(a,5)
        per.append(a)
    corr_float.append(per)

for i in range(len(corr_float)):
    zeros = [0]*(i+1)
    corr_float[i] = zeros + corr_float[i]

clustering = []
for i in range(len(corr_float)):
    clustering.append([i])
print clustering

a_flatten = reduce(add, corr_float )
a_flatten = list(dict.fromkeys(a_flatten))
a_flatten.sort(reverse=True)

z = 0
while True:
    z = z +1
    print z

    value = a_flatten[0]

    indexes = []
    for i in range(len(corr_float)):
        for j in range(len(corr_float[i])):
            if corr_float[i][j] == value:
                u = (i,j)
                indexes.append(u)

    a_flatten.pop(0)

    for i in range(len(indexes)):
        print i
        pem = []
        for j in range(len(clustering)):
            if indexes[i][0] in clustering[j]:
                pem.append(clustering[j])
                n = j
                break
        clustering.pop(n)
        for j in range(len(clustering)):
            if indexes[i][1] in clustering[j]:
                pem.append(clustering[j])
                m = j
                break
        clustering.pop(m)
        pem = pem[0]+pem[1]
        clustering.append(pem)

    print len(clustering)

    if len(clustering) <17:
        break

for i in range(len(clustering)):
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\Clustering\cluster%s.txt"%i,"w")
    for j in range(len(clustering[i])):
        a = str(clustering[i][j])
        f.write(a)
        f.write("\n")
    f.close()










