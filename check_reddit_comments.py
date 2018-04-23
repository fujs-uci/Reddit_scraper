"""Bag of words"""
import sqlite3 as sql
import nltk


if __name__ == "__main__":

        conn = sql.connect("comments.db")
        c = conn.cursor()
        c.execute("SELECT DISTINCT imdb_id FROM comments")
        imdb_id = c.fetchall()

        complete = 0
        for mov_id in imdb_id:
                c.execute("SELECT id FROM comments where imdb_id = ?",(mov_id[0],))
                total = len(c.fetchall())
                complete += total

        print(complete/3619)
        conn.close()

        #loop through the data base of comments that are associated with movies
                #nltk.CountVectorizer5
