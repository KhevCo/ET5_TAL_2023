# Before starting anything, execute init_tp.py to download all the required packages

Note : all python programms need an input file and an outpule file when executed. The tag converter files and Stanford jars paths are written in the code to avoid the user from searching thoses files and pasting their paths. However, the users can manually change the path for a converting file inside the python scripts if he wants to.

### pos_ref_to_txt.py
Transforms an annoted reference file to an untaged txt file.

### pos_ref_to_univ.py
Converts an annoted reference file to contain universal tags.

### txt_to_postag_nltk.py
Converts a txt file into a taged file with nltk.

### txt_to_postag_stanford.py
Converts a txt file into a taged file with Stanford.

### postag_to_univ.py
Converts pos_tag tags to universal tags. This should be used for both nltk and Stanford.

### conll_to_txt.py
Transforms an annoted reference file (CONLL) to an untaged txt file.

### txt_to_ne_nltk_conll.py
Reads a txt file, uses the named entity recognition from nltk, and convert the NER tags into BIO-tags. Stores the result in a file that should have exactly the same format as the reference file (ne_reference.txt.conll).

### txt_to_nertag_stanford_conll.py
Reads a txt file, uses the named entity recognition from Stanford, and convert the NER tags into BIO-tags. Stores the result in a file that should have exactly the same format as the reference file (ne_reference.txt.conll).

### evaluate.py
A file not made by myself, I only changed the variables and paths to make it run. Compares how similar are the contents of two files, it compares the words (first column) and the tags (second column). It can be used between the reference file and nltk/Stanford, or between Stanford and nltk.
