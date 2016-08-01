import psycopg2
import sys

try:
    arg = sys.argv[1]
except IndexError:
    arg = ""

conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
cur = conn.cursor()

if not arg=="":
	cur.execute("SELECT word,count FROM Tweetwordcount WHERE word = %s", (arg,))
	value = cur.fetchone()
	if value is None:
	   value=(arg,0)
	print "Total number of occurences of \"%s\": %d" % (value[0],value[1])
else:
	cur.execute("SELECT word,count FROM Tweetwordcount order by word asc")
        value = cur.fetchall()
        for x in value:
		print x
conn.close()

