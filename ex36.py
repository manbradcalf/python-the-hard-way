from sys import exit

def helipad():
	print "Finally, you manage to escape  them"
	print "You find yourself on a helipad with\nonly a few moments to spare"
	print "The helicopter's door is open, beckoning"
	print "You notice a revolver on the fire escape below"
	print "You have to make a decision\nwhat do you do?"
	print ">>Hijack helicopter?"
	print ">>Grab gun?"

	helipad_choice = raw_input("> ")
	gallons = 0
	bullets = 0

	if 'hijack' in helipad_choice:

		global gallons
		gallons = 5

		print "You don't know how,\nbut you start the helicopter"
		print "You check the fuel gauge\nyou have 5 gallons"
		print "The manual says this helicopter gets 10mpg"
		print "Boris waits in a warehouse 20 miles from here"
		print "Vlad waits in the jungle 10 miles away"
		hijacked()


	elif 'gun' in helipad_choice:

		global bullets
		bullets = 5

		print "Good choice, now you're armed!"
		print "But -- shit! So are they! And they're yelling!"
		print "Their footsteps creep close to your fire escape"
		print "Do you jump to the platform below?"
		print "Do you shoot the two men looking for you?"

		grabbed_gun()

	else:
		print "get it together man!"
		print "make up your mind!"

def hijacked():
	global gallons
	print "You have %d gallons" % gallons
	print "Where do you go?"
	hijacked_choice = raw_input('> ')

	if 'warehouse' in hijacked_choice:
		global gallons
		gallons = gallons - 2
		print "'You have %d gallons left' he says" % gallons
		print "'How do you know?' you ask.\nBoris says there is no time to explain"
		print "Boris asks if he can take you somewhere"
		print "Do you oblige?"
		boris_ride()


	elif 'jungle' in hijacked_choice:
		global gallons
		gallons = gallons - 1
		print "You arrive in the jungle safely"
		print "Vlad screams 'You have %d gallons left!" % gallons
		print "You shake your head in disbelief"

	else:
		print "Make up your mind!"

def boris_ride():
	oblige_boris = raw_input("> ")
	if 'yes' in oblige_boris:
		global gallons
		gallons = gallons - 1
		print "Boris shoves chloroform in your face"
		print "You wake up in a palace"
		print "Boris winks as he tells you \nthat there are %d gallons left" % gallons
		

	if 'no' in oblige_boris:
		dead('Boris shoots you and u die')








def grabbed_gun():
	print bullets


def dead(why):
	print why
	exit(0)

helipad()
