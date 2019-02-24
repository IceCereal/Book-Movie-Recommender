from ast import literal_eval as lit_eval
import csv

importantData = []
genre = []
language = []
country = []

allGenres = []

header = ['Wikipedia Movie ID', 'Movie Name', 'Release Date', 'Languages', 'Country of Origin', 'Genre']

with open("movie.metadata.tsv") as Fobj:
		rd = csv.reader(Fobj, delimiter="\t", quotechar='"')
		for row in rd:
			genre = []
			language = []
			country = []

			rawDict = row[8]
			Dict = lit_eval(rawDict)
			for entry in Dict:
				genre.append(Dict[entry])

			rawDict = row[6]
			Dict = lit_eval(rawDict)
			for entry in Dict:
				language.append(Dict[entry])

			rawDict = row[7]
			Dict = lit_eval(rawDict)
			for entry in Dict:
				country.append(Dict[entry])
		
			for entry in genre:
					if entry not in allGenres:
						allGenres.append(entry)

			importantData.append([[row[0], row[2], row[3], language, country, genre]])


### WRITE ALL THE REQUIRED METADATA OF THE MOVIE
with open("MovieMetadata.csv", 'a') as Fobj:
	writer = csv.writer(Fobj)
	
	writer.writerow(header)

	for row in importantData:
		writer.writerow(row)

"""### WRITE ALL THE MOVIES' GENRES
with open("AllMovieGenres.csv", 'w') as Fobj:
	writer = csv.writer(Fobj)

	for genre in allGenres:
		writer.writerow([genre])
"""