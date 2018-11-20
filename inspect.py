# inspect a sentence fragment
# USAGE EXAMPLE: python3 ./inspect.py vectors/bnc.txt vectors/dimensions.txt

import sys
import itertools
import numpy as np
from utils import read_vectors, read_dimensions, cosine_similarity, coherence

vectors = read_vectors(sys.argv[1])
dimensions = read_dimensions(sys.argv[2])
threshold = 0.2

def find_common(v1,v2):
    #for i,v in np.ndenumerate(v1):
    #    print(dimensions[i[0]],v)
    dims1 = [dimensions[i[0]] for i,v in np.ndenumerate(v1) if v >= threshold]
    dims2 = [dimensions[i[0]] for i,v in np.ndenumerate(v2) if v >= threshold]
    return set.intersection(set(dims1),set(dims2))


fragment = "play_N arrive_V large_A prompt_V"

words = fragment.split()
if len(words) > 1:
    for w1,w2 in itertools.combinations(words,2):
        if w1 != w2 and w1 in vectors and w2 in vectors:
            cos = cosine_similarity(vectors[w1],vectors[w2])
            print(w1,w2,cos)
            print(find_common(vectors[w1],vectors[w2]))
