from ast import literal_eval as le
import csv

allGenres = []
genres = []

count = 0

with open ("booksummaries.txt") as fObj:
	reader = csv.reader(fObj, delimiter='\t')

	for row in reader:
		genres = []		
		count += 1

		if count % 1000 == 0:
			print (allGenres, len(allGenres), "\n\n\n")

			print ("\n\n", count, "\n\n")

			with open("AllBookGenres.csv", 'w') as fObj2:
				writer  = csv.writer(fObj2)

				for genre in allGenres:
					writer.writerow([genre])
		rawDict = row[5]

		try:
			Dict = le(rawDict)
		except:
			continue

		for entry in Dict:
			genres.append(Dict[entry])

		for genre in genres:
			if genre not in allGenres:
				allGenres.append(genre)		
"""



with open ("booksummaries.txt") as fObj:
	reader = csv.reader(fObj, delimiter='\t')

	for row in reader:
		print (row[5], type(row[5]))
		break

"""

