import numpy as np
import itertools
from math import sqrt

def read_vectors(vecfile):
    vectors = {}
    with open(vecfile) as f:
        veclines=f.read().splitlines()

    #Make dictionary with key=row, value=vector
    for l in veclines:
        items=l.split()
        row=items[0]
        vec=[float(i) for i in items[1:]]
        vec=np.array(vec)
        vectors[row]=vec
    return vectors

def read_dimensions(dimfile):
    with open(dimfile) as f:
        dimensions=f.read().splitlines()
    return dimensions[0].split()

def cosine_similarity(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of same length")
    num = np.dot(v1, v2)
    den_a = np.dot(v1, v1)
    den_b = np.dot(v2, v2)
    return num / (sqrt(den_a) * sqrt(den_b))

def coherence(sentence, vectors):
    cosines = []
    words = sentence.split()
    if len(words) > 2:
        for w1,w2 in itertools.combinations(words,2):
            if w1 != w2 and w1 in vectors and w2 in vectors:
                cos = cosine_similarity(vectors[w1],vectors[w2])
                #print(w1,w2,cos)
                cosines.append(cos)
    if len(cosines) > 0:
        return sum(cosines) / len(cosines)
    else:
        return 0

