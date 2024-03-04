import nltk
from nltk import pos_tag
from nltk import RegexpParser

def extract_chunks_from_txt(in_file_name, out_file_name) :
	file = open(in_file_name)
	contenu = file.read().split('\n')
	file.close()
	
	grammar = "Compound: {<DT>?<JJ>*<NN>}"
	chunker = RegexpParser(grammar)
	file_res = ""
	for sentence in contenu :
		result = chunker.parse(pos_tag(sentence.split()))
		for element in result :
			file_res+=(str(element) + "\n")
	
	# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
	file = open(out_file_name,'w')
	file.write(file_res[:-1]) # on retire le saut de ligne à la fin
	file.close()

extract_chunks_from_txt('wsj_0010_sample.txt', 'wsj_0010_sample.txt.chk.nltk')

print("success !")
