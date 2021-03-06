# READ TEXT FROM FILE
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# Reading text from a file is very easy with Python (much easier than other
# languages like Java) - here we go through a file line-by-line and count
# the number of gendered pronouns in the text.
#
# Look in the 'SourceTexts' folder for more example source files.
#
# CHALLENGE:
# 1. What else might you look for in the text?
# 2. Can you load two text files and compare them automatically?


import re										# load some extra code for 'regular expressions'

filename = "SourceTexts/TimeMachine.txt"		# file to load - use a full path or store locally
lines = []										# empty list to store lines from the file

numLines = 0									# variables to keep track of # lines, gender pronoun count
maleCount = 0
femaleCount = 0
neutralCount = 0

# open the file using the filename specified
file = open(filename)

# go through the file line-by-line...
for line in file:
	numLines += 1										# increment the line count for the file
	
	line = line.lower()									# convert to lowercase so we match "He" and "he"
	
	male = re.findall('he|him|his|himself', line)		# the '|' means OR
	maleCount += len(male)								# since findall returns a list, the length of that list is the # of matching pronouns!
	
	female = re.findall('she|her|hers|herself', line)
	femaleCount += len(female)
	
	neutral = re.findall('it|its|itself', line)
	neutralCount += len(neutral)

# remember to ALWAYS close the file when done
file.close()

# print the results!
print "# of lines in file: " + str(numLines)
print "Male:               " + str(maleCount)
print "Female:             " + str(femaleCount)
print "Neutral:            " + str(neutralCount)
