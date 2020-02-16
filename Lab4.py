#Zad1
test = "I am what I am"
split = test.split(" ")
words = {}

for word in split:
    if word not in words:
        words[word] = 0

    words[word] += 1

print(words)

#Zad2
def extractWordFeatures(x):
    n = 3
    worddic = {}
    par = x.replace(" ", "")

    for i in range(0, len(par) - n + 1):
        word = par[i:i+n]
        if word not in worddic:
            worddic[word] = 0

        worddic[word] += 1
    print(worddic)

phrase = input('Enter phrase to extract: ')
extractWordFeatures(phrase)

#Zad3(hard)
import numpy as np

def kmeans(examples, K, maxIters):
    from copy import deepcopy

    # Euclidean Calc.
    def distance(a, b, ax=1):
        return np.linalg.norm(a - b, axis=ax)

    C_x = np.random.randint(0, np.max(examples)-20, size=K)
    C_y = np.random.randint(0, np.max(examples)-20, size=K)
    C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
    print("Initial Centroids")
    print(C)

    C_old = np.zeros(C.shape)
    clusters = np.zeros(len(examples))
    error = distance(C, C_old, None)
    while True:
        if error == 0 or maxIters == 0:
            break
        for i in range(len(examples)):
            distances = distance(examples[i], C)
            cluster = np.argmin(distances)
            clusters[i] = cluster
        C_old = deepcopy(C)
        for i in range(K):
            points = [examples[j] for j in range(len(examples)) if clusters[j] == i]
            C[i] = np.mean(points, axis=0)
        error = distance(C, C_old, None)
        maxIters -= 1

    print("Result")
    print(C)

import pandas as pd

data = pd.read_csv('data.csv')
data.head()

f1 = data['Vector1'].values
f2 = data['Vector2'].values
data.head()
examples = np.array(list(zip(f1, f2)))
kmeans(examples, 3, 10)