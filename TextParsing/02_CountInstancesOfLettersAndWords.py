# COUNT INSTANCES OF LETTERS AND WORDS
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# Counting words can show patterns and themes in texts; here we count
# vowels, then words.  A more advanced example that counts only words
# over a certain length can be found in the "CreateDictionary" example.
#
# CHALLENGE:
# 1. Can you count the # of upper- and lower-case letters?
# 2. Can you count two or more words that seem meaningful in the source and compare
#    the results automatically? 


# source sentence
sentence = "One ring to rule them all, one ring to find them, one ring to bring them all and in the darkness bind them."

# find all commas
for character in sentence:		# goes through the string character-by-character
	if character == ',':		# if the current character is a comma
		print "comma!"


# find all vowels
vowelCount = 0														# variable to store the count
sentence = sentence.lower()											# convert to all lowercase (so that 'A' and 'a' both match)
for c in sentence:													# iterate characters
	if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':	# if they match vowels...
		vowelCount = vowelCount + 1									# increment the count!
print '# of vowels: ' + str(vowelCount)								# ... and print the results


# does the string contain a certain word?
if 'ring' in sentence:				# looks for any instance of the word
	print 'word "the" found!'

# that's great, but it doesn't tell us where or how often it occurs!

# split sentence by spaces
words = sentence.split()
print words

# count instances of the word 'ring'
ringCount = 0									# like vowels, count instances of word
for word in words:								# go through all resulting words one-by-one
	if word == 'ring':							# if the current word is 'ring'
		ringCount += 1							# increment the count - a cleaner method than used above
print 'count for "ring": ' + str(ringCount)