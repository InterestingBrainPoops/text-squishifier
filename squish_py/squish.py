from squish_py import bitmanip as bm
def encode(line):
	bts = bm.tobits(line)
	ratios = {
		"rat":[bts.count(0)/len(bts), bts.count(1)/len(bts)], # ratio for 0, ratio for 1
		"goal":[0,1]
	}
	#print(str(bts.count(0)) + " " + str(bts.count(1)))
	for x in range(len(bts)):#print(ratios)
		cbt = bts[x]
		if(cbt == 0):
			#print("0")
			ratios["goal"] = [ratios["goal"][0], ratios["goal"][0] + ratios["rat"][0]*(ratios["goal"][1]-ratios["goal"][0])]
		elif(cbt == 1):
			ratios["goal"] = [ratios["goal"][0] + ratios["rat"][0]*(ratios["goal"][1]-ratios["goal"][0]), ratios["goal"][1]] 
			#print("1")
		else:
			print(cbt)
		#print(ratios["goal"])
	ratios["goal"] = (ratios["goal"][0]+ratios["goal"][1])/2
	#print(ratios)
	return ratios
	
def decode(json):
	ratios = json["rat"]
	goal = json["goal"]
