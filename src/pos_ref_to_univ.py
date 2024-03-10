import sys
import re

if (len(sys.argv) < 3) :
    print("Paramètres attendus:\npos_ref_to_univ.py input_file output_file")
else :
	def convert_tags_ref_to_univ(in_file_name, out_file_name, converter_ref_ptb, converter_ptb_univ):
		convert_file = open("../data/" + converter_ref_ptb)
		convert_lines_ref_ptb = convert_file.read().split('\n')
		convert_file.close()
		convert_tags = []
		for line in convert_lines_ref_ptb :
			convert_tags.append(re.split(r' +', line))
		file = open("../data/" + in_file_name)
		contenu = file.read().split('\n')
		file.close()
		temp_res = ""
		for line in contenu :
			words = line.split('\t')
			try :
				found = False
				for corresp in convert_tags :
					if (words[1] == corresp[0]) :
						temp_res+=(words[0] + "\t" + corresp[1] + "\n")
						found = True
				if (not found) : # si jamais on ne trouve pas de correspondance, on garde le tag tel quel
					temp_res+=(words[0] + "\t" + words[1] + "\n")
					print("failed to convert tag : ", words[1])
			except : # ça échoue quand words[1] n'est pas défini, c'est à dire quand on a un saut de ligne
				temp_res+="\n"
	
		convert_file = open("../data/" + converter_ptb_univ)
		convert_lines_ptb_univ = convert_file.read().split('\n')
		convert_file.close()
		convert_tags = []
		for line in convert_lines_ptb_univ :
			convert_tags.append(re.split(r' +', line))
		contenu = temp_res.split("\n")
		contenu = contenu[:-1] # on retire un saut de ligne à la fin
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
					out_res+=(words[0] + "\t" + words[1] + "\n")
			except : # ça échoue quand words[1] n'est pas défini, c'est à dire quand on a un saut de ligne
				out_res+="\n"
				
		# le paramètre 'w' de open() sert à écrire par-dessus le contenu actuel du fichier, ou le créer si le fichier n'existe pas.
		file = open("../data/" + out_file_name,'w')
		file.write(out_res[:-1]) # on retire un saut de ligne à la fin, il en reste désormais un qui annonce la fin de la phrase courante
		file.close()

	convert_tags_ref_to_univ(sys.argv[1], sys.argv[2], 'POSTags_REF_PTB.txt', 'POSTags_PTB_Universal.txt')

	print("success !")