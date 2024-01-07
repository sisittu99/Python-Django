import sys

def all_in():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if len(sys.argv) == 2:
		lista = sys.argv[1].split(',')
		for i in lista:
			found = False
			i = i.strip()
			if i == '':
				continue
			i = i.capitalize()
			if i in states.keys():
				print(i + " is a state and its capital is " + capital_cities[states[i]])
				found = True
			elif i in capital_cities.values():
				for j in capital_cities.items():
					if j[1] == i:
						for k in states.items():
							if k[1] == j[0]:
								print(i + " is the capital of " + k[0])
								Found = True
								break
						break
			if not found:
				print(i + " is neither a capital city nor a state")

if __name__ == '__main__':
	all_in()
