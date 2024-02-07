import sys

# Inizializza un generatore di numeri pseudo-casuali basato sull'ora corrente
def custom_random_seed(casual):
	current_time = int(casual * 1000) # Converte il tempo corrente in millisecondi
	seed = (current_time * 1103515245 + 12345) & 0x7fffffff # Moltiplica e applica un'operazione di bitmask
	return seed

def custom_random(casual):
	seed = custom_random_seed(casual)
	while True:
		seed = (seed * 1103515245 + 12345) & 0x7fffffff
		yield seed

def colore_esadecimale_random(casual):
	random_generator = custom_random(casual)
	colore = next(random_generator) % 0xFFFFFF
	if colore > 0xDDDDDD:
		colore -= 0xDDDDDD
	colore_esadecimale = "#{:06x}".format(colore)
	return colore_esadecimale

class PeriodicTableElement:
	def __init__(self, line):
		array = line.split(', ')
		# first position contains "Name = position:x". Save it
		self.name = array[0].split(' = ')[0]
		self.position = int(array[0].split(' = ')[1].split(':')[1])
		# second position contains "number:x". Save it
		self.number = int(array[1].split(':')[1])
		# third position contains "small: x". Save it
		self.small = array[2].split(': ')[1]
		# fourth position contains "molar:x". Save it
		self.molar = float(array[3].split(':')[1])
		# fifth position contains "electron:x". Save it
		self.electrons = array[4].split(':')[1]

	def __str__(self):
		return self.name + " " + str(self.position) + " " + str(self.number) + " " + self.small + " " + str(self.molar) + " " + self.electrons

	def printElement(self):
		print(self.__str__())

	def __eq__(self, other):
		return self.name == other.name and self.position == other.position and self.number == other.number and self.small == other.small and self.molar == other.molar and self.electrons == other.electrons

	def createHtmlElement(self):
		html = "<td style=\"border: 1px solid black; padding:10px; background-color:" + str(colore_esadecimale_random(self.molar * 249 % 1027)) +"\">\n"
		html += "<h4 style=\"text-align: center; color:#FFFFFF\">" + self.name + "</h4>\n"
		html += "<ul style=\"list-style:none; color:#FFFFFF\">\n"
		html += "<li>" + str(self.number) + "</li>\n"
		html += "<li style=\"font-size:45px\">" + self.small + "</li>\n"
		html += "<li>" + str(self.molar) + "</li>\n"
		html += "</ul>\n"
		html += "</td>\n"
		return html

def parsePeriodicTable():
	periodic_table = []
	with open("periodic_table.txt", "r") as file:
		last = 0
		for line in file:
			tmpObj = PeriodicTableElement(line)
			if (tmpObj.position != last):
				for i in range(last, tmpObj.position):
					periodic_table.append(PeriodicTableElement(" = position:" + str(i) + ", number:0, small: , molar:0, electron:"))
			periodic_table.append(tmpObj)
			last = 0 if tmpObj.position == 17 else tmpObj.position + 1
	return periodic_table

if __name__ == "__main__":
	elementsArray = parsePeriodicTable()
	for i in elementsArray:
		i.printElement()
	html = "<!DOCTYPE html>\n"
	html += "<html>\n"

	html += "<head>\n"
	html += "<title>Periodic Table</title>\n"
	html += "</head>\n"

	html += "<body>\n<table>\n"

	for i in range(0, 7):
		html += "<tr>\n"
		for j in range(0, 18):
			if (elementsArray[i * 18 + j].number != 0):
				html += elementsArray[i * 18 + j].createHtmlElement()
			else:
				html += "<td></td>\n"
		html += "</tr>\n"

	html += "</table>\n</body>\n"
	html += "</html>\n"
	with open("periodic_table.html", "w") as file:
		file.write(html)
