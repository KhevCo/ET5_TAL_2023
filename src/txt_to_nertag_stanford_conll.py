import nltk
import sys
import re
from nltk.tokenize import word_tokenize as wtk
from nltk.tag import StanfordNERTagger

if (len(sys.argv) < 3) :
    print("Paramètres attendus:\ntxt_to_nertag_stanford_conll.py input_file output_file")
else :
	def extract_ner_tags_stanford(in_file_name,out_file_name, convert_file_name) :
		file = open("../data/" + in_file_name)
		contenu = file.read().split('\n')
		file.close()
		file_res = ""
		stanford_ner = StanfordNERTagger("../data/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz", "../data/stanford-ner-2020-11-17/stanford-ner.jar")
		previous = ""
		i=0 # i sert à voir l'avancée du programme car c'est long
		tot = len(contenu)
		for sentence in contenu :
			i=i+1
			print(i, " / ", tot)
			sentence_tokenized = wtk(sentence)
			namedEnt = stanford_ner.tag(sentence_tokenized)
			for element in namedEnt:

				# on retire tous les cas qui décalent d'une ligne, en ignorant le mot de plus. On diminue ainsi la précision des mots en transformant "I'" and "I" pour éviter d'avoir "I" puis "'". Comme c'est aux tags d'entités nommés qu'on s'intéresse, cela n'est pas gênant. On note dans previous le tag précédent pour savoir si le $ et le & sont problématiques ou non.
				
				if (element[0] == "$" and (previous == "AU" or previous == "CA" or previous == "US")) : # US$, CA$ et AU$ se faisaient séparer en deux mots
					pass
				elif (element[0] == ";" or element[0] == "''" or element[1] == "''" or (element[0] == "'" and previous=="I")) : # ";" se faisait séparer en `` et ; et '', on décide de ne garder que le ``. Permet également de résoudre le problème du "I'm"
					pass
				elif (element[0] == "&" or previous == "&") : # R&D se faisaient séparer en deux mots donc on skip "&" ainsi que le "D"
					pass
				else : # dans ce cas, tout se passe bien
					file_res+=(element[0] + "\t" + element[1] + "\n")
				previous = element[0]
			file_res+="\n"


		# on convertit les étiquettes en format univ et on ajoute le biotag
		convert_file = open("../data/" + convert_file_name)
		convert_lines = convert_file.read().split('\n')
		convert_tags = []
		for line in convert_lines :
			convert_tags.append(re.split(r' +', line))
		contenu = file_res.split('\n')
		out_res = ""
		prefix = "B-"
		previous_tag = "A_DUMB_TAG_I_INVENTED_THAT_DOESN'T_EXISTS" # de sorte à garantir que words[1] soit différent de previous_tag lors du premier tour de boucle
		for line in contenu :
			words = line.split('\t')
			found = False
			try :
				if (words[1] == "O") :
					prefix = ""
				elif (words[1] == previous_tag) :
					prefix = "I-"
				else :
					prefix = "B-"
				for corresp in convert_tags :
					if (words[1] == corresp[0]) :
						out_res+=(words[0] + "\t" + prefix + corresp[1] + "\n")
						found = True
				if (not found) : # si jamais on ne trouve pas de correspondance, on garde le tag tel quel
					out_res+=(words[0] + "\t" + prefix + words[1] + "\n")
				previous_tag = words[1]
			except : # une ligne vide
				out_res+="\n"

		# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
		out_file = open("../data/" + out_file_name,'w')
		out_file.write(out_res[:-2]) # on retire les saut de ligne à la fin
		out_file.close()		



	extract_ner_tags_stanford(sys.argv[1],sys.argv[2], 'NERTags_PTB_Universal_Linux.txt')

	print("success !")