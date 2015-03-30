print "You walk into a dingy, wood paneled room. \nThe only furniture in the room is a small recliner on which an old man sits,\nstaring back at you."
print "He looks vaguely familiar. What do you say? \n 1. 'hello'\n 2. 'what are you doing here?'"

speak = raw_input("> ")

if speak == "1":
	print "He begins to shrink into the recliner. He yells coldly. He becomes more distant"
	print "Once he is the size of a walnut, he asks you your name You tell him..."

	name = raw_input("> ")

	if name == 'Ben':
		print "'hello ben...wanna chill?' says the old man"
		print "you respond to the old man with..."
		print "1. 'nah dog'"
		print "2. 'yah dog'"

		ben_response = raw_input("> ")

		if ben_response == "1":
			print "He shoots you immediately with no hesitation"
			print "u ded"

		if ben_response == "2":
			print "the old man grins slyly and opens up a wormhole"
			print "'take this' says the old man, and tosses you a zordon blaster"

	elif name == 'Liz':
		print "The old man responds 'shit...ok well here...\ntake all of my money'"
		print "Liz, What do you do with the money?"
		print "1. spend it on booze"
		print "2. throw it in the air"
		print "3. diversify yo bonds"

		liz_response = raw_input("> ")

		if liz_response == "1" or liz_response == "2":
			print "Yo that's tite"

		elif liz_response == "3":
			print "Aite, aite. smoove moove"

		else:
			print "dowut?!"

	else:
		print "GTFO IDK U DAWG"




elif speak == "2":
	print "You stare into the endless abyss at oldman's retina."
	print "1. blueberries."
	print "2. yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"
