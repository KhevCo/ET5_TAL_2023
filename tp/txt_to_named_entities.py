import nltk
from nltk.tokenize import word_tokenize as wtk
from nltk import pos_tag

def extract_named_entities(in_file_name, out_file_name) :
	file = open(in_file_name)
	contenu = file.read().split('\n')
	file.close()
	file_res = ""
	for sentence in contenu :
		sentence_tokenized = wtk(sentence)
		tokens_tag = pos_tag(sentence_tokenized)
		namedEnt = nltk.ne_chunk(tokens_tag, binary=False)
		
		for element in namedEnt :
			if isinstance(element, nltk.tree.tree.Tree):
				for leaf in element:
					file_res+=(leaf[0] + " ")
				file_res=file_res[:-1] # on retire l'espace à la fin
				file_res+=("\t" + element.label() + "\n")
	
	# on écrit le résultat des entitées nommées
	file = open(out_file_name,'w')
	file.write(file_res[:-1]) # on retire le saut de ligne à la fin
	file.close()

extract_named_entities('wsj_0010_sample.txt','wsj_0010_sample.txt.ne.nltk')
extract_named_entities('formal-tst.NE.key.04oct95_small.txt','formal-tst.NE.key.04oct95_small.txt.ne.nltk')

print("success !")
