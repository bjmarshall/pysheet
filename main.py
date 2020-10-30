from rolls import evalRolls, rollStats

character = {
	"str": 10,
	"dex": 10,
	"con": 10,
	"int": 10,
	"wis": 10,
	"cha": 10,

	"level": 1,

	"hp": 1,
	"temp hp": 0,
	"death saves": [0,0],

	"conditions": []
}

def modFromStat(stat):
	return (stat // 2) - 5

def grabCharacterStats():
	return [character["str"], character["dex"], character["con"],
	        character["int"], character["wis"], character["cha"]]

def showStats():
	ret = "Level: " + str(character["level"]) + "\tHP: " + str(character["hp"])

	if character["temp hp"] > 0:
		ret += ("\tTemp HP: " + character["temp hp"])

	ret += "\n"

	stats = grabCharacterStats()
	statline = "Stats: STR {0} ({1})\t DEX {2} ({3})\t CON {4} ({5})\t INT {6} ({7})\t WIS {8} ({9})\t CHA {10} ({11})"

	ret += statline.format(stats[0], modFromStat(stats[0]),
	                       stats[1], modFromStat(stats[1]),
						   stats[2], modFromStat(stats[2]),
						   stats[3], modFromStat(stats[3]),
						   stats[4], modFromStat(stats[4]),
						   stats[5], modFromStat(stats[5]))

	ret += "\n"

	if character["conditions"] != []:
		ret += ("Conditions: " + ', '.join(character["conditions"]))
		ret += "\n"

	if character["death saves"] != [0,0]:
		ret += "Death saves: {0} successes, {1} failures.".format(character["death saves"][0], character["death saves"][1])

	print(ret)

# Translates names to the dictionary key that accesses a field. This way, "str" and "strength" can access the same field.
def interpretName(name):
	ndict = {"strength": "str", "dexterity": "dex", "constitution": "con",
	         "intelligence": "int", "wisdom": "wis", "charisma": "cha", "chr": "cha",
			 "health": "hp", "temp": "temp hp", "temp_hp": "temp hp"}

	return ndict.get(name, name)

while(True):
	s = input().lower()	# Get user input

	if(s[0:4] == "set "):
		s = s[4:]
		s = s.split()
		character[interpretName(s[0])] = int(s[1])

	elif(s[0:4] == "get "):
		s = s[4:]
		s = s.split()
		print(str(character[interpretName(s[0])]))

	# Interpret inputs
	elif(s == "stats"):
		showStats()
	elif(s[0:5] == "eval "): # provides access to python evaluation without having to exit
		print(eval(s[5:]))
	elif any(str.isdigit(c) for c in s):
		print(evalRolls(s))
