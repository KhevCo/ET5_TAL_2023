import re

def convert_tags_ne_to_univ(in_file_name, out_file_name, convert_file_name):
	convert_file = open(convert_file_name)
	convert_lines = convert_file.read().split('\n')
	convert_tags = []
	for line in convert_lines :
		convert_tags.append(re.split(r' +', line))
	in_file = open(in_file_name)
	contenu = in_file.read().split('\n')
	in_file.close()
	out_res = ""
	for line in contenu :
		words = line.split('\t')
		found = False
		for corresp in convert_tags :
			if (words[1] == corresp[0]) :
				out_res+=(words[0] + "\t" + corresp[1] + "\n")
				found = True
		if (not found) : # si jamais on ne trouve pas de correspondance, on garde le tag tel quel
			out_res+=(words[0] + "\t" + words[1] + "\n")
		
	out_file = open(out_file_name,'w')
	out_file.write(out_res[:-1]) # on retire le saut de ligne à la fin
	out_file.close()

convert_tags_ne_to_univ('wsj_0010_sample.txt.ne.nltk', 'wsj_0010_sample.txt.ne.univ', 'NERTags_PTB_Universal_Linux.txt')
convert_tags_ne_to_univ('formal-tst.NE.key.04oct95_small.txt.ne.nltk','formal-tst.NE.key.04oct95_small.txt.ne.univ', 'NERTags_PTB_Universal_Linux.txt')

print("success !")
