"""check unqiue comment db"""
import sqlite3 as sql
from collections import defaultdict

def returnDict():
        finaldict = defaultdict(str)

        com = sql.connect("comments.db")
        c = com.cursor()

        c.execute("SELECT * FROM comments")
        results = c.fetchall()

        for result in results:
                finaldict[result[1]] += result[2]
                
        com.close()

        return finaldict

x = returnDict()



while(True):
        print(len(x.keys()))
        print(len(x.values()))
        for x,y in x.items():
                print(x)
                print(len(y.split()))
                if(input("continue")=="y"):
                        print(y)

        if(input("result")) == "n": break
