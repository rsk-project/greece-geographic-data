import unicodecsv as csv
import codecs

with open('ota.csv') as f:
	r = csv.reader(f, encoding='utf-8')

	with codecs.open('comunity.csv', mode="w", encoding="utf-8") as out:
		uniq = []
		for line in r:
			if line[17] not in uniq:
				print >> out, u"%s,%s,%s,%s" % (line[17], line[18], line[19], line[20])
				uniq.append(line[17])