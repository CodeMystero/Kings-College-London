import numpy as np

d = list(range(554))
trajectories = []
data = []

for i in range(len(d)):
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\databyframe\data%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for i in range(len(lines)):
        L.append(lines[i].split('\n')[0])

    data.append(L)


data = np.array(data).T.tolist()

for i in range(len(data)):
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\databytranjectory\data%s.txt"%i,"w")
    for j in range(len(data[i])):
        a = str(data[i][j])
        a = a.strip("v ")
        f.write(a)
        f.write("\n")
f.close()

