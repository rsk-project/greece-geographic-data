import unicodecsv as csv
import codecs

with open('3-villages.csv') as f:
	r = csv.reader(f, encoding='utf-8')

	values = []
	with codecs.open('3-villages.sql', mode="w", encoding="utf-8") as out:
		print >> out, "insert into roma.villages(`id`, `name`, `population`, `municipality_id`) values ",
		for line in r:
			values.append("(%s, '%s', '%s', '%s')" % (line[0], line[1], line[2], line[3]))
		print >> out, ",".join(values),
		print >> out, ";",