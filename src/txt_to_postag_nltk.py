import nltk
from nltk.tokenize import word_tokenize as wtk
from nltk import pos_tag
import sys

if (len(sys.argv) < 3) :
    print("Paramètres attendus:\ntxt_to_postag_nltk.py input_file output_file")
else :
	def extract_pos_tags_nltk(in_file_name,out_file_name):
		file = open("../data/" + in_file_name)
		contenu = file.read().split('\n')
		file.close()
		file_res = ""
		grammar = """
		Adjectif-Nom-Nom: {<JJ>(<NN>|<NNS>|<NNP>|<NNPS>)(<NN>|<NNS>|<NNP>|<NNPS>)}
		Adjectif-Adjectif-Nom: {<JJ><JJ>(<NN>|<NNS>|<NNP>|<NNPS>)}
		Adjectif-Nom: {<JJ>(<NN>|<NNS>|<NNP>|<NNPS>)}
		Nom-Nom: {(<NN>|<NNS>|<NNP>|<NNPS>)(<NN>|<NNS>|<NNP>|<NNPS>)}
		"""
		for sentence in contenu :
			sentence_tokenized = wtk(sentence)
			tokens_tag = pos_tag(sentence_tokenized)
			for element in tokens_tag:
				file_res+=(element[0] + "\t" + element[1] + "\n")
		
		# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
		file = open("../data/" + out_file_name,'w')
		file.write(file_res[:-1]) # on retire le saut de ligne à la fin
		file.close()

	extract_pos_tags_nltk(sys.argv[1],sys.argv[2])

	print("success !")