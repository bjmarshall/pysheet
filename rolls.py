import random
import re

def roll(word):

	parts = word.split("d") # "XdY" becomes ("x", "y") and "XdY+Z" becomes ("X", "Y+Z")

	numDice = int(parts[0])

	part2 = parts[1].split("+")
	if len(part2) == 2:
		numFaces = int(part2[0])
		constAdd = int(part2[1])
	else:
		part2 = parts[1].split("-")
		if len(part2) == 2:
			numFaces = int(part2[0])
			constAdd = int(part2[1]) * -1
		else:
			numFaces = int(part2[0])
			constAdd = 0

	result = 0
	for x in range(int(numDice)):
		result += random.randint(1, int(numFaces))
	return result + constAdd

def evalRolls(sentence):
	words = sentence.split()

	for i, word in enumerate(words):
		if re.match("[0-9]+d[0-9]+", word) and (i == 0 or words[i - 1] != "on"):
			words[i] = str(roll(word))
	return ' '.join(words)

def rollStats():
	rolls = [-1,-1,-1,-1]
	stats = []

	for x in range(6):
		# roll four dice.
		for i in range(4):
			rolls[i] = random.randint(1,6)
		stats.append(sum(rolls) - min(rolls))

	return stats
