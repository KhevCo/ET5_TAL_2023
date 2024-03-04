### >>> Before starting anything, execute init_tp.py to download all the required packages <<<

Note : all python programms are executable without any arguments. For further tests (if needed), change the arguments passed in the call of function (call of function is always the last line before printing "success !")

### txt_to_pos_tag.py
Transforms a text file to tagged words with nltk.post_tag.

### postag_to_univ.py
Converts nltk.pos_tag tags to universal tags, using the POSTags_PTB_Universal_Linux.txt file.

### conll_to_txt.py
Transforms a conll tag file to paragraphs of text, and removes all the tags.

### conll_to_postag.py
Transforms a conll tag file to annotations using nltk.pos_tag tags.

### txt_to_chunk.py
Transforms a text file to chunks, using a basic grammar {<DT>?<JJ>*<NN>} to recognize compound words. Stores it into raw strings.

### txt_to_chunk-gen.py
Transforms a text file to chunks, using a extended ( = generalized) grammar to recognize compound words. This version includes singular/plural nouns, and singuar/plural proper nouns. Stores the data filtered by grammar.

###txt_to_named_entities.py
Reads a text file to look for named entities using nltk.ne_chunk, and stores only the named entities in the output file.

### named_entities_to_univ.py
Converts nltk.ne_chunk tags to universal tags, using the NERTags_PTB_Universal_Linux.txt file.

### ne_univ_to_csv.py
Using the given universal tags, counts every occurrence of each named entity, calculate the frequency of each, and stores it into a csv file. First line of the csv file indicates the column names.
