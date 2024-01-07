import sys

def state():
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
		capital_city = sys.argv[1]
		for i in capital_cities.items():
			if i[1] == capital_city:
				for j in states.items():
					if j[1] == i[0]:
						print(j[0])
						return
				break
		print("Unknown state")


if __name__ == '__main__':
	state()
