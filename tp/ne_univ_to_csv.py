def convert_ne_univ_to_csv (in_file_name, out_file_name):
	file = open(in_file_name)
	contenu = file.read().split('\n')
	file.close()
	tags = []
	for line in contenu :
		tags.append(line.split('\t'))
	tot = len(tags)
	count_tags = dict()
	for word in tags :
		try :
			count_tags[word[0]][1]+=1
		except :
			count_tags[word[0]] = [word[1],1]
	out_res = "Entité nommée,Type,Nombre d’occurrences,Proportion dans le texte (%)\n"
	for w in count_tags :
		out_res+=(w + "," + count_tags[w][0] + "," + str(count_tags[w][1]) + "," + str(format(count_tags[w][1]*100/tot, '.3f')) + "\n")
	out_file = open(out_file_name,'w')
	out_file.write(out_res)
	out_file.close()

convert_ne_univ_to_csv ('wsj_0010_sample.txt.ne.univ', 'wsj_0010_sample.txt.ne.csv')
convert_ne_univ_to_csv ('formal-tst.NE.key.04oct95_small.txt.ne.univ', 'formal-tst.NE.key.04oct95_small.txt.ne.csv')

print("success !")