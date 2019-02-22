"""from ast import literal_eval as le
import subprocess
import csv
import sys
#import asyncio

importantData = []
genre = []

allGenres = []

count = 0

with open("movie.metadata.tsv") as fd:
    	rd = csv.reader(fd, delimiter="\t", quotechar='"')
    	for row in rd:
        	rawDict = row[8]
        	Dict = le(rawDict)

        	for entry in Dict:
            	genre.append(Dict[entry])
		for entry in genre:
			if entry not in allGenres:
				allGenres.append(entry)

        	#importantData.append([row[0], row[2], genre])

print (allGenres)"""

"""inputNum = int(sys.argv[1]) + 5000

count = inputNum

if (inputNum + 15000 > len(importantData)):
	end = len(importantData)
else:
	end = inputNum + 15000

with open("DataSplit/"+str(inputNum)+".csv", 'a') as Fobj:
	writer = csv.writer(Fobj)
	for row in importantData[inputNum: end]:
		print (count)
		writer.writerow(row)
		count += 1
"""
from ast import literal_eval as le
import csv

allGenres = []
genres = []

count = 0

with open("movie.metadata.tsv") as fObj:
	reader = csv.reader(fObj, delimiter='\t', quotechar='"')

	for row in reader:
		genres = []
		count += 1
		if count %1000 == 0:
			print (len(allGenres), "\n\n", allGenres, "\n\n")
			print ("\n\n", count, "\n\n")

			with open("AllGenres.csv", 'w') as fObj2:
				writer = csv.writer(fObj2)

				for genre in allGenres:
					writer.writerow([genre])

		rawDict = row[8]
		Dict = le(rawDict)

		for entry in Dict:
			genres.append(Dict[entry])

		for genre in genres:
			if genre not in allGenres:
				allGenres.append(genre)

