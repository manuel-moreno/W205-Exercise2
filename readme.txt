Main Appliscation Execution:

After downloading the contents of the repository, update the credentials in the tweet.py spout

From the main repository folder, execute the following commands:

$cd Example2/spouts
$vim tweet.py

Update lines 13-16 using your application credentials from apps.twitter.com

Navigate to the StreamParse main folder (Example2) and execute the following command to initiate the StreamParse application and connect to Twitter:

$sparse run

Data serving scripts:

finalresults.py
When executed with arguments, this script will return the number of occurrences for the first argument provided. When executed with no arguments, this script will return the full list of words, on for each line.

Execution:
	python finalresults.py old

	python finalresults.py

histogram.py
This script will take a single argument that consists of two integers separated by a comma (e.g. 4,6). After validating the argument, this script will return items that occurred a number of times that falls between the two integers provided (inclusive) or indicate that no items were found.

Execution:
	python histogram.py 5,20

barplot.py
This script will simply create a bar chart of the 20 most common words. This will be saved to testplot.png.

Execution:
	python barplot.py


