import sys

if (len(sys.argv) < 3) :
    print("Paramètres attendus:\npos_ref_to_txt.py input_file output_file")
else :
	def convert_tags_ref_to_txt(in_file_name, out_file_name):
		file = open("../data/" + in_file_name)
		contenu = file.read().split('\n')
		file.close()
		out_res = ""
		for line in contenu :
			words = line.split('\t')
			if (words==['']) :
				out_res+="\n"
			elif (words[1] == "SENT" or words[1] == "COMMA" or words[1] == "COLON") :
				out_res = out_res[:-1] # on retire l'espace avant la ponctuation
				out_res+=(words[0]+" ")
			else :
				out_res+=(words[0]+" ")
				
		# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
		file = open("../data/" + out_file_name,'w')
		file.write(out_res[:-1]) # on retire le saut de ligne à la fin
		file.close()
	
	convert_tags_ref_to_txt(sys.argv[1],sys.argv[2])

	print("success !")