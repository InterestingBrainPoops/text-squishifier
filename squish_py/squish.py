from squish_py import bitmanip as bm
import sys
import mpmath
class Error(Exception):
    """Base class for other exceptions"""
    pass
class StringTooLargeError(Error):
    """Raised when the String length is too long. This should be removed soon as a better system using binary 
		is put into place. 
		 """
    pass
def encode(line):
	mpmath.mp.dps = 1000
	bts = bm.tobits(line) # bts becomes the bitarray of line/ the string. 
	#print([bts.count(0), bts.count(1)])
	ratios = {
		"rat":[mpmath.mpf(bts.count(0)/len(bts)), mpmath.mpf(bts.count(1)/len(bts))], # ratio for 0, ratio for 1
		"goal":[mpmath.mpf(0),mpmath.mpf(1)] # Not really the goal, but rather the current active range for the solution. 
	}
	#print(bts[0])
	#print(len(bts)) # For testing purposes, remove sooner then later
	for x in range(len(bts)): # Loops through the bitarray
		cbt = bts[x]
		if(cbt == 0): # modifies goal to the lower portion 
			#print("0")
			ratios["goal"] = [ratios["goal"][0], ratios["goal"][0] + ratios["rat"][0]*(ratios["goal"][1]-ratios["goal"][0])]
		elif(cbt == 1): # Modifiies goal to the higher position.
			ratios["goal"] = [ratios["goal"][0] + ratios["rat"][0]*(ratios["goal"][1]-ratios["goal"][0]), ratios["goal"][1]] 
			#print("1")
		else:
			print(cbt) # This should never happen. 
		if(ratios["goal"][0] == ratios["goal"][1]):
			print("Bad things have happened at the pos:" + str(x))
			raise StringTooLargeError
			break
		#print(ratios["goal"])
		#print(cbt)
	#print(ratios["goal"])
	#print(len(bts))
	ratios["length"] = len(bts)
	ratios["goal"] = (ratios["goal"][0]+ratios["goal"][1])/2 # Sets goal to the average of the min and max
	#print(ratios)
	#print((sys.getsizeof(line)-sys.getsizeof(ratios))/sys.getsizeof(line) )  # being used to see compression percentage.
	return ratios
	
def decode(json):
	ratios = json["rat"]
	goal = json["goal"]
	mpmath.mp.dps = 1000
	nx = [mpmath.mpf(0), mpmath.mpf(1)]
	decider = ratios[0] # starts off as the % of 0s in the msg. 
	le = json["length"]
	bts = []
	for x in range(le):
		if(goal < decider and goal > nx[0]):
			#print(0)
			bts.append(0)
			nx = [nx[0], nx[0] + ratios[0]*(nx[1]-nx[0])]
			decider = nx[0]+ratios[0]*(nx[1]-nx[0])
		elif(goal > decider and goal < nx[1]):
			#print(1)
			bts.append(1)
			nx = [nx[0] + ratios[0]*(nx[1]-nx[0]), nx[1]]
			decider = nx[0]+ratios[0]*(nx[1]-nx[0])
		else:
			print("Something went wrong")
	#print(len(bts))
	#print(bm.frombits(bts))
	return bm.frombits(bts)
	