import nltk
from nltk.tokenize import word_tokenize as wtk
from nltk import pos_tag

def convert_tags_conll_to_pos_tag(in_file_name, out_file_name):
	file = open(in_file_name)
	contenu = file.read().split('\n')
	file.close()
	res = ""
	for line in contenu :
		try :
			words = line.split('\t')
			if (words[3] == "PONCTU") :
				if (res[-1]=="\n") :
					pass # on vient passer la répétition de ponctuation après un saut de ligne
				else :
					res = res[:-1] # on retire l'espace avant la ponctuation
					res+=(words[1]+" ")
			else :
				res+=(words[1]+" ")
		except : # on exécute ce cas là si on a une ligne vide
			res+="\n"
	while (res[-1]=="\n") :
		res = res[:-1]
	contenu = res.split('\n')
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

convert_tags_conll_to_pos_tag('wsj_0010_sample.txt.conll', 'wsj_0010_sample.txt.pos')

print("success !")