import psycopg2
import sys
import numpy as np
import matplotlib.pyplot as plt


conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word,count FROM Tweetwordcount order by count desc limit 20")
value = cur.fetchall()
found = 0
if not value is None:
	found = 1
conn.close()
if found == 0:
	print "Nothing to return"
else:

	# sort in-place from highest to lowest
	value.sort(key=lambda x: x[1], reverse=True) 

	# save the names and their respective scores separately
	# reverse the tuples to go from most frequent to least frequent 
	words = zip(*value)[0]
	count = zip(*value)[1]
	x_pos = np.arange(len(words)) 

	plt.bar(x_pos, count,align='center')
	plt.xticks(x_pos, words) 
	plt.ylabel('Word Occurrence')
	plt.savefig('testplot.png')
