i = 0
with open('periphereies.json') as in_file:
	for line in in_file.readlines():
		i = i + 1
		with open('regions/%d.json' % i , 'w') as out_file:
			print >> out_file, line