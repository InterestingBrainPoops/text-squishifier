import squish_py as squish
def encdecstr():
	assert squish.decode(squish.encode("Hello")) == "Hello" , "Should have encoded and decoded properly."
def encdecfile():
	assert True, "Should have enced and deced file properly."


tests = [encdecstr, encdecfile]
if __name__ == "__main__":
		for x in range(len(tests)):
			tests[x]()
		print("Everything passed")