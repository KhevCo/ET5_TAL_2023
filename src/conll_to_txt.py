import nltk
import sys

if (len(sys.argv) < 3) :
    print("Paramètres attendus:\nconll_to_txt.py input_file output_file")
else :
	def convert_tags_conll_to_txt(in_file_name, out_file_name):
		file = open("../data/" + in_file_name)
		contenu = file.read().split('\n')
		file.close()
		out_res = ""
		for line in contenu :
			if (line == "\t\t") :
				out_res+="\n"
			else :
				words = line.split('\t')
				out_res+=(words[0]+" ")

		# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
		file = open("../data/" + out_file_name,'w')
		file.write(out_res[:-1]) # on retire le saut de ligne à la fin
		file.close()
	
	convert_tags_conll_to_txt(sys.argv[1], sys.argv[2])
	
	print("success !")