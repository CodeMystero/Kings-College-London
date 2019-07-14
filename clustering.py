
from operator import add

d = list(range(424))
corr = []
K =[]
for i in range(len(d)):
    print i
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\correlation_reduced\data%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for i in range(len(lines)):
        L.append(lines[i].split('\n')[0])
        K.append(lines[i].split('\n')[0])
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
        a = round(a,4)
        per.append(a)
    corr_float.append(per)

K = [float(i) for i in K]
K = [round(i, 4) for i in K]

for i in range(len(corr_float)):
    zeros = [0]*(i+1)
    corr_float[i] = zeros + corr_float[i]

clustering = []
for i in range(len(corr_float)):
    clustering.append([i])
print clustering

a_flatten = list(dict.fromkeys(K))
a_flatten.sort(reverse=True)

z = 0
while True:
    z = z +1
    print "how many iteratiorn ? : %s"%z

    value = a_flatten[0]

    indexes = []
    for i in range(len(corr_float)):
        for j in range(len(corr_float[i])):
            print i
            if corr_float[i][j] == value:
                u = (i,j)
                indexes.append(u)
    print "index done"
    a_flatten.pop(0)

    for i in range(len(indexes)):
        pem = []
        for j in range(len(clustering)):
            print i
            if indexes[i][0] in clustering[j]:
                pem.append(clustering[j])
                n = j
        clustering.remove(pem[0])
        for j in range(len(clustering)):
            print i
            if indexes[i][1] in clustering[j]:
                pem.append(clustering[j])
                m = j
        if len(pem) == 2:
            clustering.remove(pem[1])



        pem = reduce(add, pem)
        pem = list(dict.fromkeys(pem))
        clustering.append(pem)
    print "clustering done"
    print len(clustering)


    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\Clustering\cluster%s.txt" % z, "w")
    for i in range(len(clustering)):
        a = str(clustering[i])
        f.write(a)
        f.write("\n")
    f.close()

    if len(a_flatten) == 0:
        break
    if len(clustering) < 2:
        break








