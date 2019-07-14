import numpy as np
from numpy import linalg as LA

d = list(range(424))
final_data = []
final_data_1d = []
for i in range(len(d)):
    print i
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\databysensors_reduced\sensor%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for j in range(len(lines)):
        L.append(lines[j].split('\n')[0])


    ### Use the Karhunen-Loeve Transform
    data = []
    for i in range(len(L)):
        l = L[i]
        b = l.split()
        pem = []
        for k in range(len(b)):
            a = float(b[k])
            pem.append(a)
        data.append(pem)

    data_min = []
    a = []
    b = []
    c = []
    for i in range(len(data)):
        a.append(data[i][0])
        b.append(data[i][1])
        c.append(data[i][2])
    data_min.append(sum(a)/len(a))
    data_min.append(sum(b)/len(b))
    data_min.append(sum(c)/len(c))

    ### Zero-mean data
    zeromean_data = []
    for i in range(len(data)):
        per = []
        x = data[i][0]-data_min[0]
        y = data[i][1]-data_min[1]
        z = data[i][2]-data_min[2]
        per = [x, y, z]
        zeromean_data.append(per)

    ### Covariance Matrix
    #   a   b   c
    #   d   e   f
    #   g   h   i
    covar_data = []
    cor_a = []
    cor_b = []
    cor_c = []
    cor_d = []
    cor_e = []
    cor_f = []
    cor_g = []
    cor_h = []
    cor_i = []
    for i in range(len(zeromean_data)):
        cor_a.append(zeromean_data[i][0] * zeromean_data[i][0])
        cor_b.append(zeromean_data[i][0] * zeromean_data[i][1])
        cor_c.append(zeromean_data[i][0] * zeromean_data[i][2])
        cor_d.append(zeromean_data[i][1] * zeromean_data[i][0])
        cor_e.append(zeromean_data[i][1] * zeromean_data[i][1])
        cor_f.append(zeromean_data[i][1] * zeromean_data[i][2])
        cor_g.append(zeromean_data[i][2] * zeromean_data[i][0])
        cor_h.append(zeromean_data[i][2] * zeromean_data[i][1])
        cor_i.append(zeromean_data[i][2] * zeromean_data[i][2])

    cor_a = sum(cor_a)/len(cor_a)
    cor_b = sum(cor_b)/len(cor_b)
    cor_c = sum(cor_c)/len(cor_c)
    cor_d = sum(cor_d)/len(cor_d)
    cor_e = sum(cor_e)/len(cor_e)
    cor_f = sum(cor_f)/len(cor_f)
    cor_g = sum(cor_g)/len(cor_g)
    cor_h = sum(cor_h)/len(cor_h)
    cor_i = sum(cor_i)/len(cor_i)

    covar_data = [[cor_a,cor_b,cor_c],[cor_d,cor_e,cor_f],[cor_g,cor_h,cor_i]]


    ##eig values and vectors
    A = np.array(covar_data)
    w, v = LA.eig(A)
    w_list = w.tolist()

    p = w_list[0]
    q = w_list[1]
    r = w_list[2]

    if isinstance(p,complex):
        w_list[0] = p.real
    if isinstance(q,complex):
        w_list[1] = q.real
    if isinstance(r,complex):
        w_list[2] = r.real

    min_index = w_list.index(min(w_list))
    max_index = w_list.index(max(w_list))

    v_reduced = np.delete(v,min_index,1)
    index_1d = []

    if max_index == 0:
        index_1d.append(1)
        index_1d.append(2)
    if max_index == 1:
        index_1d.append(0)
        index_1d.append(2)
    if max_index == 2:
        index_1d.append(0)
        index_1d.append(1)

    v_reduced_1d = np.delete(v,index_1d[0],1)
    v_reduced_1d = np.delete(v,index_1d[1],1)

    v_reduced_list = v_reduced.tolist()
    v_reduced_list_1d = v_reduced_1d.tolist()

    # examplars pernetration
    reduced_data = []

    for i in range(len(data)):
        y = []
        y_1 = v_reduced_list[0][0]*data[i][0]+v_reduced_list[1][0]*data[i][1]+v_reduced_list[2][0]*data[i][2]
        y_2 = v_reduced_list[0][1]*data[i][0]+v_reduced_list[1][1]*data[i][1]+v_reduced_list[2][1]*data[i][2]
        y.append(y_1)
        y.append(y_2)
        reduced_data.append(y)
    final_data.append(reduced_data)


    reduced_data_1d = []

    for i in range(len(data)):
        j = []
        j_1 = v_reduced_list_1d[0][0]*data[i][0]+v_reduced_list_1d[1][0]*data[i][1]+v_reduced_list_1d[2][0]*data[i][1]
        j.append(j_1)
        reduced_data_1d.append(j)
    final_data_1d.append(reduced_data_1d)



for i in range(len(final_data)):
    print i
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\PCA2D_reduced\sensor%s.txt"%d[i],"w")
    for k in range(len(final_data[i])):
        a = str(final_data[i][k])
        a = a.strip("[")
        a = a.strip("]")
        a = a.replace(',','')
        print a
        f.write(a)
        f.write("\n")
f.close()

for i in range(len(final_data_1d)):
    print i
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\PCA1D_reduced\sensor%s.txt"%d[i],"w")
    for k in range(len(final_data_1d[i])):
        a = str(final_data_1d[i][k])
        a = a.strip("[")
        a = a.strip("]")
        a = a.replace(',','')
        print a
        f.write(a)
        f.write("\n")
f.close()
