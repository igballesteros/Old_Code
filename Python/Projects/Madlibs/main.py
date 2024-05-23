#with provides context
#any operations on variable f within with block
#automatically cleans everything up  outside block

with open("story.txt", "r") as f:
	story = f.read()
	print(story)


words = set() #only contains unique elements
startWord = -1
targetStart = "<"
targetEnd = ">"

#look for all of the words in the story

#finds the <>
#for loop goes through character index
#enumerate - access to position and element
for i, char in enumerate(story):
	if char == targetStart:
		startWord = i

	if char == targetEnd and startWord != -1:
		word = story[startWord: i + 1] #slice - subsection of whole
		words.add(word)
		startWord = -1

answers = {}

for word in words: #dictionary creation
	answer = input("Enter a word for " + word + ": ")
	answers[word] = answer

for word in words:
	story = story.replace(word, answers[word])

print(story)