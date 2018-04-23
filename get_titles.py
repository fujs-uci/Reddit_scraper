import csv

def get_titles_and_year(file):
    length = 0
    total = 0
    # tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres
    with open(file, encoding='utf-8') as tsvfile, open('movie_year.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvfile = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        tsvfile = csv.reader(tsvfile, delimiter="\t", quotechar='"')
        for row in tsvfile:
            total += 1
            if total % 1000 == 0: print(total)
            titleType = row[1]
            title = row[2]
            year = row[5]
            genre = None
            if titleType == 'movie' and year != '\\N' and int(year) > 2005:
                length += 1
                if len(row) == 9:
                        genre = row[8]
                csvfile.writerow([title, year, genre])
    
    print("closing...")
    print(length)
            
    return






get_titles_and_year("data.tsv")
# get_titles_and_year("tester.txt")
