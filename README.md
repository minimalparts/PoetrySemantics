# The semantics of poetry

This is the repo accompanying the paper "[The semantics of poetry: a distributional reading](https://aurelieherbelot.net/resources/papers/LLC2014_poetry.pdf)" (Herbelot 2014).  If you use this code, please cite the following:

Herbelot, A., 2014. The semantics of poetry: A distributional reading. Digital Scholarship in the Humanities, 30(4), pp.516-531.

**Abstract:**

Poetry is rarely a focus of linguistic investigation. This is far from surprising,
as poetic language, especially in modern and contemporary literature, seems to
defy the general rules of syntax and semantics. This paper assumes, however, that
linguistic theories should ideally be able to account for creative uses of language,
down to their most difficult incarnations. It proposes that at the semantic level,
what distinguishes poetry from other uses of language may be its ability to trace
conceptual patterns which do not belong to everyday discourse but are latent in
our shared language structure. Distributional semantics provides a theoretical and
experimental basis for this exploration. First, the notion of a specific ‘semantics of
poetry’ is discussed, with some help from literary criticism and philosophy. Then,
distributionalism is introduced as a theory supporting the notion that the meaning
of poetry comes from the meaning of ordinary language. In the second part of the
paper, experimental results are provided showing that a) distributional representa-
tions can model the link between ordinary and poetic language, b) a distributional
model can experimentally distinguish between poetic and randomised textual out-
put, regardless of the complexity of the poetry involved, c) there is a stable, but
not immediately transparent, layer of meaning in poetry, which can be captured
distributionally, across different levels of poetic complexity.

## Data

For copyright reasons, the poetry data is not included in this repository, with the exception of Brooke's *Day that I have loved* (1911) which is now in the public domain. The random and factual texts inspected in Section 3.1 of the paper are also included. This data can be found in the data/ directory, under the relevant subdirectory. The texts have been pre-processed as explained in the paper, keeping only nouns, verbs, adjectives and adverbs.

The BNC vectors used in the paper can be found in vectors/bnc.tar.gz. This file must be untarred before use:

    tar -xzf bnc.tar.gz
    
In the vectors/ directory, the user will also find the labels of the vector space's dimensions, in the file dimensions.txt.


## Usage

To replicate results from the paper, use compute_coherence.py over the relevant text. For instance:

    python3 compute_coherence.py data/poems/brooke.processed vectors/bnc.txt

It is also possible to look at shared contexts between word vectors (as in Table 4 of the paper), by running:

    python3 inspect.py vectors/bnc.txt vectors/dimensions.txt

You can change the inspected fragment in the inspect.py file itself.
