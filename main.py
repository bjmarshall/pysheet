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

# all attacks of the form ["Name", "bonus to hit", "formula for damage"]
attacks = [ ["Unarmed Strike", "5", "1d1 + 2"],
            ["Longsword (1h)", "7", "1d8 + 4"]]

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
	strr = input().lower()	# Get user input
	s = strr.split()

	if(s[0] == "set"):
		character[interpretName(s[1])] = int(s[2])

	elif(s[0] == "get"):
		print(str(character[interpretName(s[1])]))

	elif(s[0] == "add"):
		if (s[1] == "cond") or (s[1] == "condition"):
			character[conditions].append(s[1])

	elif (s[0] == "attack") or (s[0] == "attacks") or (s[0] == "att") or (s[0] == "atk"):
		if len(s) > 1:
			for atk in attacks:
				if s[1] in atk[0].lower():
					print( ("You attack with {0}! {1} to hit for {2} damage.").format(*[evalRolls(field) for field in atk]) )
					# prevent multiple attacks from being shown
		else:
			for atk in attacks:
				if atk[1][0] != '-':
					atk[1] = ('+' + atk[1])
				print( ("{0}: {1} to hit, {2} damage").format(*atk) )

	# Interpret inputs
	elif s[0] == "stats":
		showStats()
	elif s[0] == "eval": # provides access to python evaluation without having to exit
		print(eval(strr[5:]))
	else:
		print(evalRolls(strr))
