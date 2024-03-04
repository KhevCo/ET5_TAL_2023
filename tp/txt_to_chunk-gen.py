import nltk
from nltk import pos_tag
from nltk import RegexpParser

def extract_chunks_from_txt_gen (in_file_name, out_file_name) :
	file = open(in_file_name)
	contenu = file.read().split('\n')
	file.close()
	
	grammar = """
	Adjectif-Nom-Nom: {<JJ>(<NN>|<NNS>|<NNP>|<NNPS>)(<NN>|<NNS>|<NNP>|<NNPS>)}
	Adjectif-Adjectif-Nom: {<JJ><JJ>(<NN>|<NNS>|<NNP>|<NNPS>)}
	Adjectif-Nom: {<JJ>(<NN>|<NNS>|<NNP>|<NNPS>)}
	Nom-Nom: {(<NN>|<NNS>|<NNP>|<NNPS>)(<NN>|<NNS>|<NNP>|<NNPS>)}
	"""

	chunker = RegexpParser(grammar)
	file_res = dict()
	for sentence in contenu :
		result = chunker.parse(pos_tag(sentence.split()))
		
		for element in result :
			if isinstance(element, nltk.tree.tree.Tree):
				leaves = []
				for leaf in element :
					leaves.append(leaf[0])
				try :
					file_res[element.label()]+=[leaves]
				except :
					file_res[element.label()]=[leaves]
	
	# on transforme le dictionnaire (key,value) en un string qui trie les valeurs en fonction de la clé, pour avoir le format de sortie désiré
	str_file_res = ""
	try :
		for e in file_res.keys() :
			str_file_res+=(e + ":\n")
			for values in file_res[e] :
				for word in values :
					str_file_res+=(word + " ")
				str_file_res=str_file_res[:-1] # on retire l'espace à la fin
				str_file_res+="\n"
			str_file_res+="\n"
		str_file_res=str_file_res[:-2] # on retire les 2 sauts de ligne à la fin
	except :
		pass
	file = open(out_file_name,'w')
	file.write(str_file_res)
	file.close()

extract_chunks_from_txt_gen('wsj_0010_sample.txt', 'wsj_0010_sample.txt.chk.nltk')

print("success !")
