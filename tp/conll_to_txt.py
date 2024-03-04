import nltk

def convert_tags_conll_to_txt(in_file_name, out_file_name):
	file = open(in_file_name)
	contenu = file.read().split('\n')
	file.close()
	out_res = ""
	for line in contenu :
		try :
			words = line.split('\t')
			if (words[3] == "PONCTU") :
				if (out_res[-1]=="\n") :
					pass
				else :
					out_res = out_res[:-1] # on retire l'espace avant la ponctuation
					out_res+=(words[1]+" ")
			else :
				out_res+=(words[1]+" ")
		except : # on exécute ce cas là si on a une ligne vide
			out_res+="\n"
	# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
	file = open(out_file_name,'w')
	file.write(out_res[:-1]) # on retire le saut de ligne à la fin
	file.close()

convert_tags_conll_to_txt('wsj_0010_sample.txt.conll', 'wsj_0010_sample.txt')

print("success !")