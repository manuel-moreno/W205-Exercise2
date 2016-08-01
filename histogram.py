import psycopg2
import sys

try:
    arg = sys.argv[1]
except IndexError:
    arg = ""

ints = [int(s) for s in arg.split(',') if s.isdigit()]

conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
cur = conn.cursor()

if len(ints)==2:
	if ints[0] > ints[1]:
		ints = [ints[1],ints[0]]
	cur.execute("SELECT word,count FROM Tweetwordcount order by word asc")
        value = cur.fetchall()
	found = 0
	if not value is None:
        	for x in value:
			if x[1] >= ints[0] and x[1] <= ints[1]:
				found = 1
				print  "%s: %d" % (x[0],x[1])
	if found == 0:
		print "Nothing to return"
else:
	print "Invalid argument, please use format 'min,max'"
conn.close()

