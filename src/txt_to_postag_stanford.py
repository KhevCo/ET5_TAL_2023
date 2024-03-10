import nltk
from nltk.tokenize import word_tokenize as wtk
from nltk.tag import StanfordPOSTagger
import sys

if (len(sys.argv) < 3) :
    print("Paramètres attendus:\ntxt_to_postag_stanford.py input_file output_file")
else :
	def extract_pos_tags_stanford(in_file_name,out_file_name):
		file = open("../data/" + in_file_name)
		contenu = file.read().split('\n')
		file.close()
		file_res = ""
		stanford_pos = StanfordPOSTagger("../data/stanford-postagger-full-2020-11-17/models/english-bidirectional-distsim.tagger", "../data/stanford-postagger-full-2020-11-17/stanford-postagger.jar")
		i=0
		tot = len(contenu)
		for sentence in contenu :
			i=i+1
			print(i, " / ", tot)
			sentence_tokenized = wtk(sentence)
			tokens_tag = stanford_pos.tag(sentence_tokenized)
			for element in tokens_tag:
				file_res+=(element[0] + "\t" + element[1] + "\n")
		
		# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
		file = open("../data/" + out_file_name,'w')
		file.write(file_res[:-1]) # on retire le saut de ligne à la fin
		file.close()

	extract_pos_tags_stanford(sys.argv[1],sys.argv[2])

	print("success !")