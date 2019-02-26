# Book-Movie-Recommender
<h6>A project developed for Enigma's HackWeek Edition 1. [Topic: Recommender Systems]</h6>

# Why
After reading a book, many readers would like to watch a movie that is very similar to the books they saw online.
Book-Movie-Recommender recommends a book based on the input as the summary of the book.

# How it works
There are two datasets involved:
[CMU's Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/ "CMU Movie Summary Corpus") and
[CMU's Book Summary Dataset](https://www.cs.cmu.edu/~dbamman/booksummaries.html "CMU Book Summary Dataset") <br><br>
A summary is chosen from the book dataset, and then it's cosine similarity with a movie summary is calculated. 
The cosine similarities are ranked and the 5 highest values are shown.

# Limitations & Fixes
Brute force, i.e. `value = cosine_similarity(Book_Summary, Movie_Summary)` for all `Movie_Summary`'s takes too much time.
An alternative is to sort all movies by genre's and process it according to genres. However, `Anime` is a genre of a 
movie that does not exist for book. The last attempt which seems to give approximately good results is to create a relative 
cosine_similarity Hash Table. Calculate a the cosine_similarity with respect to the first summary and store the 
`cos_sim*1000` in a Hash Table. Then check the `value*1000` in the hash table. 

# Current Files
The current files do not include the Hash Table. <br><br>

The current files are
- `Calculate-RelativeCos-Movies.py` which is the relative cosine calculator.
- `Driver-RelativeCos.py` which is the driver to find out the best match.

