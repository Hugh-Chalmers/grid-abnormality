import sys, random
choice = raw_input("Randomly generate a grid or use current one implimented? R/I\n").lower()
defaultitem = "X"
if choice == "i": # g is grid
	g = """
	X X X X X
	X X X X X
	X X N X X
	X X X X X
	X X X X X
	""" 
if choice == "r": # g is grid
	g = ""
	across = random.randrange(3,10) # Edit to whatever
	down = random.randrange(3,10) # Edit to whatever
	abnormality = random.randrange(1,across*down) # Generated a numeric value for where to place the abnormality
	c = 0 # Counter to check where to place N
	for l in range(down):
		g += "\n" # Adds a newline after each row of X's
		for o in range(across):
			c += 1 # Numeric ID of the current grid item
			if c == abnormality: # If the grid item's ID is the abnormality
				g += "N" 
			else:
				g += defaultitem 
	g = g.replace(" ", "") # Cleans up any errors with spacing
	print(" ".join(g)) # Inserts spaces properly
if choice == "r" or choice == "i":
	v = 1 # Vertical counter: It's 0 because we ignore the first \n
	h = 0 # Horizontal counter
	g = g[1:] # Strips the first, unwanted \n character
	for l in range(len(list(g))):
		currentItem = g[l]  # The current item in the grid, e.g. "X" 
		if currentItem == defaultitem or currentItem == "N" or currentItem == "\n": # Ignores spaces
			if currentItem == "\n": # Indicates start of new row
				v += 1 
				h = 0 # Resets horizontal counter
			else:
				h += 1 # Adds one to horizontal counter for next time
				if currentItem != defaultitem and currentItem != "\n": # Checks if the current item is the abnormality
					print "Found abnormality at coords [" + str(h) + ", " + str(v) + "] Across/Down"
		