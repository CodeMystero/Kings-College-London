import numpy as np
import random
from random import randrange
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier


######### NN
class Perceptron(object):

    def __init__(self, no_of_inputs =3, threshold=1000, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

d = list(range(424))
data = []
for i in range(len(d)):
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M1C1F1\DeltaModulated_reducedsensors\sensor%s.txt"%d[i],"r")
    lines = file.readlines(f)
    file.close(f)

    for j in range(len(lines)):
        L.append(lines[j].split('\n')[0])

    data.append(L)

for i in range(len(d)):
    L = []
    f = open("C:\Users\hwani\Desktop\Project\Dataset\P1M2C1F1\DeltaModulated_reducedsensors\sensor%s.txt"%d[i],"r")
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

## M1 = 0, M2 = 1

data_float_array = np.array(data_float) #array

label_m1 = [0]*424
label_m2 = [1]*424
label = label_m1 + label_m2
##########################TRAINING#######################
## training _NN

training_inputs = []
for i in range(len(data_float_array)):
    training_inputs.append(data_float_array[i])

labels = np.array(label) #array

perceptron = Perceptron(553)
perceptron.train(training_inputs, labels)

## training _ SVM
X = data_float #list
y = label #list
clf_svm = svm.SVC(gamma = 'scale')
clf_svm.fit(X,y)

## training Gaussian naive bayesean

X_NB = training_inputs
y_NB = labels
clf_NB = GaussianNB()
clf_NB.fit(X_NB,y_NB)

## training decision tree

X_tree = data_float
y_tree = label
clf_tree = tree.DecisionTreeClassifier()
clf_tree = clf_tree.fit(X_tree,y_tree)

## SGD classifier

X_SGD = training_inputs
y_SGD = labels
clf_SGD = linear_model.SGDClassifier(max_iter = 1000, tol = 1e-3)
clf_SGD.fit(X_SGD,y_SGD)

## KNN Classifier
X_neigh = data_float
y_neigh = label
neigh = KNeighborsClassifier(n_neighbors = 3)
neigh.fit(X_neigh,y_neigh)

#######################PREDICTION
##prediction
population = []
for i in range(100):
    num_zeros = randrange(554)
    input = [0.]*num_zeros + [1.]*(553-num_zeros)
    random.shuffle(input)
    population.append(input)

howmanyone = []
for i in range(len(population)):
    pem = []
    a = perceptron.predict(population[i]) ## prediction NN
    b = clf_svm.predict([population[i]]) ## prediction SVM
    c = clf_NB.predict([population[i]])
    d = clf_tree.predict([population[i]])
    e = clf_SGD.predict([population[i]])
    f = neigh.predict([population[i]])
    pem.append(int(a))
    pem.append(int(b))
    pem.append(int(c))
    pem.append(int(d))
    pem.append(int(e))
    pem.append(int(f))
    howmanyone.append(sum(pem))
## elite selection

fitness = []
for i in range(len(howmanyone)):
    a = 5-howmanyone[i]
    fitness.append(a)

fitness_sum = sum(fitness)
