from rolls import evalRolls, rollStats

while(True):
	s = input().lower()	# Get user input

	if(s[0:5] == "roll "):	# The word "roll" is optional
		s = s[5:]

	# Interpret inputs
	if(s == "stats"):
		print("Rolled:", str(rollStats()))
	if(s[0:5] == "eval "): # provides access to python evaluation without having to exit
		print(eval(s[5:]))
	elif any(str.isdigit(c) for c in s):
		print(evalRolls(s))
