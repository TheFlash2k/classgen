#!/usr/bin/env python3
'''
This will generate a cpp having class of name, whatever you name it.
AUTHOR: TheFlash2k
Github Link: https://github.com/TheFlash2k/
Written in: Python3
'''
class CPP_GEN:
	banner = "/* CPP Generator by @TheFlash2k */"
	output = f"{banner}\n#include <iostream>\n#include <string>\nusing namespace std;\n\n"
	hasAttribs = False
	hasClass = False
	className = ""
	attributes = list()
	def __init__(self, fileName):
		self.setFileName(fileName)
	'''
	This method renames the output file to a valid filename.
	In this file, the output is stored.
	'''
	def setFileName(self,fileName):
		# All these characters are not allowed in naming files
		badChars = ('\\','|','/','*','<','>','?','"',':')
		for char in badChars:
			if char in fileName:
				fileName = fileName.replace(char, '')
		self.fileName = fileName if ".cpp" in fileName else fileName + ".cpp"

	def createClass(self, className):
		self.className = className.capitalize()
		self.output += "class {}".format(self.className) + "{\n"
		self.hasClass = True

	def addAttrib(self, *attribs):
		attrib = dict()
		for i in attribs:
			attrib = i
		# Attrib now contains a dictionary of all the items
		for data in attrib.items():
			if not self.hasClass:
				print("No class has yet been initialized.")
				return None

			field = data[0].strip()
			self.attributes.append(field)
			mode  = data[1].strip()
			self.output += f"{mode}:\n\t{field};\n"
		self.hasAttribs = True
	def generateConstructor(self):
		mode = "public:\n\t"
		tAttribs = len(self.attributes)
		index = 0
		cons = f"{self.className}({self.attributes[index]} "
		index += 1
		numbers = ('int', 'double', 'float')
		for number in numbers:
			if number in cons:
				cons += "= 0"
		if index != tAttribs:
			for i in range(1, tAttribs):
				data = self.attributes[i]
				cons += f", {data} "
				if "string" in data:
					if "*" in data:
						cons += "= NULL"
					else:
						cons += "= \"\""
				elif "char" in data:
					if "*" in data:
						cons += "= \"\""
					else:
						cons += "= '_'"
				elif "*" in data:
					cons += "= NULL"
		cons += "): "
		variables = self.attributes
		for variable in variables:
			variable = variable.split()[1]
			cons += f"{variable}({variable}), "
		if cons[-2] == ',':
			cons = cons[:-2]
		cons += " {}\n"
		self.output += f"{mode}{cons}"

	# This will create the setters and getter methods
	def generateSetters(self):
		variables = self.attributes
		self.output += "public:\n"
		vars = list()
		setters = list()
		
		for variable in variables:
			vars.append(variable.split()[1])
		for var in vars:
			setters.append(f"\tvoid set{var.capitalize()}(")
		for i in range(len(self.attributes)):
			setters[i] += self.attributes[i] + "){"
			setters[i] += f"\n\t\tthis->{var} = {var};"
			self.output += setters[i] + "\n\t}\n"

	def generateGetters(self):
		variables = self.attributes
		self.output += "public:\n"
		vars = list()
		getters = list()
		datatypes = list()
		index = 0

		for variable in variables:
			vars.append(variable.split()[1])
		for types in variables:
			datatypes.append(types.split()[0])
		for var in vars:
			getters.append(f"\t{datatypes[index]} get{var.capitalize()}() const " + "{")
			index += 1
		index = 0
		for var in vars:
			getters[index] += f"\n\t\treturn this->{var};\n\t" + "}\n"
			self.output += getters[index]
			index += 1

	def createObject(self):
		if not self.hasClass:
			print("No class has yet been initialized.")
			return None
		if not self.hasAttribs:
			print("No attributes added. Creating only constructors.")
		self.generateConstructor()
		self.generateSetters()
		self.generateGetters()
		self.output += "};\n"
		self.createMain()
		self.writeToObject()
	def createMain(self):
		self.output += "\nint main(){\n\n\t" + f"{self.className} obj;\n\tstd::cout << \"Succesfully created {self.className} object!\\n\";\n\tstd::cin.get();\n\treturn 0;\n" + '}'
	def writeToObject(self):
		f = open(self.fileName, "w")
		f.write(self.output)
		f.close()
		print(f"Wrote to file {self.fileName} having class name {self.className}")

def main():
	fileName = "output" # Output file name
	className = "check" # Class name

	gen = CPP_GEN(fileName)

	# Attributes that must be added.
	attributes = {
		"int data" : "private",
		"Node* next" : "private",
		"char name" : "protected"
	}

	gen.createClass(className)
	gen.addAttrib(attributes)
	gen.createObject()

if __name__ == "__main__":
	main()
