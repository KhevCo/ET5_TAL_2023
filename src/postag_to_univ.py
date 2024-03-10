import re
import sys

if (len(sys.argv) < 3) :
    print("Paramètres attendus:\npostag_to_univ.py input_file output_file")
else :
	def convert_tags_nltk_to_univ(in_file_name, out_file_name, convert_file_name):
		convert_file = open("../data/" + convert_file_name)
		convert_lines = convert_file.read().split('\n')
		convert_tags = []
		for line in convert_lines :
			convert_tags.append(re.split(r' +', line))
		file = open("../data/" + in_file_name)
		contenu = file.read().split('\n')
		file.close()
		out_res = ""
		for line in contenu :
			words = line.split('\t')
			try :
				found = False
				for corresp in convert_tags :
					if (words[1] == corresp[0]) :
						out_res+=(words[0] + "\t" + corresp[1] + "\n")
						found = True
				if (not found) : # si jamais on ne trouve pas de correspondance, on garde le tag tel quel
					temp_res+=(words[0] + "\t" + words[1] + "\n")
					print("failed to convert tag : ", words[1])
			except : # ça échoue quand words[1] n'est pas défini, c'est à dire quand on a un saut de ligne
				out_res+="\n"
		
		# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
		file = open("../data/" + out_file_name,'w')
		file.write(out_res[:-1]) # on retire le saut de ligne à la fin
		file.close()
	
	convert_tags_nltk_to_univ(sys.argv[1], sys.argv[2], 'POSTags_PTB_Universal.txt')
	
	print("success !")