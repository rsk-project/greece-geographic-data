#!/usr/bin/python
# -*- coding: utf-8 -*-

from difflib import SequenceMatcher
import unicodecsv as csv
import codecs
import MySQLdb
import glob
import json

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

sql = 'SELECT * FROM region'
folder = 'geojson/0-regions/*'

db = MySQLdb.connect("localhost", "root", "vfimqbux", "roma", charset='utf8')

cursor = db.cursor()

cursor.execute(sql)

buff = []
for filename in glob.glob(folder):
	with open(filename) as in_file:
		data = json.loads(in_file.read())
		buff.append(data)

for item in cursor.fetchall():
	for obj in buff:
		if similar(obj['properties']['Name'].replace(u'Π. ', ''), item[1].replace(u'ΑΝ.', u'ΑΝΑΤΟΛΙΚΗΣ ')) > 0.9:
			cursor.execute("UPDATE region SET geo = '%s' WHERE id = %s" % (json.dumps(obj), item[0]))
			db.commit()