import nltk
from nltk.tokenize import word_tokenize as wtk
from nltk import pos_tag

def extract_pos_tags(in_file_name,out_file_name):
	file = open(in_file_name)
	contenu = file.read().split('\n')
	file.close()
	file_res = ""
	for sentence in contenu :
		sentence_tokenized = wtk(sentence)
		tokens_tag = pos_tag(sentence_tokenized)
		for element in tokens_tag:
			file_res+=(element[0] + "\t" + element[1] + "\n")
	
	# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
	file = open(out_file_name,'w')
	file.write(file_res[:-1]) # on retire le saut de ligne à la fin
	file.close()

extract_pos_tags('wsj_0010_sample.txt','wsj_0010_sample.txt.pos.nltk')

print("success !")