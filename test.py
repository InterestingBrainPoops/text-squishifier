import squish_py as squish

# Checks if it can encode and decode a file properly. 
def encdecfile():
	data = ""
	with open('./test.txt', 'r') as file:
		data = file.read().replace('\n', '')
	assert squish.decode(squish.encode("./test.txt")) ==  data, "Should have encoded and decoded properly."

# Add tests here once you start a new feature
tests = [ encdecfile]
if __name__ == "__main__":
		for x in range(len(tests)):# Loops through all preexisting tests. 
			tests[x]()
		print("Everything passed")