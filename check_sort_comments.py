"""Bag of words"""
import sqlite3 as sql
import nltk


if __name__ == "__main__":

        for x in range(10):
                file_name = "comment_set{}.db".format(x+1)
                conn = sql.connect(file_name)
                c = conn.cursor()
                c.execute("SELECT * FROM comments")
                result = c.fetchall()
                print( file_name, result[0] )
                conn.close()
                
##        complete = 0
##        for mov_id in imdb_id:
##                c.execute("SELECT id FROM comments where imdb_id = ?",(mov_id,))
##                total = len(c.fetchall())
##                complete += total
##
##        print(complete/3619)
##        conn.close()

        #loop through the data base of comments that are associated with movies
                #nltk.CountVectorizer
