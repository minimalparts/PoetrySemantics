# Compute coherence on a poem
# USAGE EXAMPLE: python3 ./compute_coherence.py data/poems/brooke.processed vectors/bnc.txt

import sys
import numpy as np
import itertools
from math import sqrt
from utils import read_vectors, cosine_similarity, coherence

poemfile = sys.argv[1]
vecfile = sys.argv[2]

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
    coh = coherence(line, vectors)
    if coh != 0:
        coherences.append(coh)

print("AVERAGE COHERENCE:",sum(coherences) / len(coherences))
