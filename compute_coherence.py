# Compute coherence on a poem
# USAGE EXAMPLE: python3 ./compute_coherence.py data/brooke.processed vectors/bnc.txt

import sys
import numpy as np
import itertools
from math import sqrt

poemfile = sys.argv[1]
vecfile = sys.argv[2]

vectors = {}

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

def cosine_similarity(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of same length")
    num = np.dot(v1, v2)
    den_a = np.dot(v1, v1)
    den_b = np.dot(v2, v2)
    return num / (sqrt(den_a) * sqrt(den_b))

def coherence(sentence):
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

vectors = read_vectors(vecfile)

with open(poemfile) as f:
    poem=f.read().splitlines()

# Check if poem consists of only one sentence
length_poem = len(poem)
if length_poem == 1:
    words = poem[0].split()
    chunks = [words[x:x+4] for x in range(0, len(words), 4)]
    poem = []
    for c in chunks:
        poem.append(' '.join([w for w in c]))


coherences = []
for line in poem:
    coh = coherence(line)
    if coh != 0:
        coherences.append(coh)

print("AVERAGE COHERENCE:",sum(coherences) / len(coherences))
