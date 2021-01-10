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
		self.output += "class {}".format(className.capitalize()) + "{\n"
		self.className = className.capitalize()
		self.hasClass = True
	def addAttrib(self, attribs):
		# Attrib now contains a dictionary of all the items
		for data in attribs.items():
			if not self.hasClass:
				print("No class has yet been initialized.")
				return None

			field = data[0].strip()
			self.attributes.append(field)
			# This checks if the data has an array and if that array is properly written or not.
			if '[' in field and ']' in field:
				begin = field.find('[')
				end = field.find(']') + 1
				arrayIndex = field[begin:end]
				field = field[:begin] + field[end:] + arrayIndex
			mode  = data[1].strip()
			self.output += f"{mode}:\n\t{field};\n"
		self.hasAttribs = True
	def addDirectAttrib(self, data, mode):
		self.output += f"{mode}:\n\t{data}\n"

	def addMethod(self, methods):
		index = 0
		for method in methods.items():
			rtType = method[0][0] # Return type of function
			name   = method[0][1] # Name of the function
			mode   = method[0][2] # Visbility mode of the function
			args = ""
			if not method[1]:
				args += "(){" + '}'
			else:
				args += '('
				for arg in method[1]:
					args += arg + ', '
				args = args[:-2] + '){' + '}'
			self.output += f"{mode}:\n\t{rtType} {name} {args}\n"

	def addDirectMethod(self, data, mode):
		if '{' != data[-2] and '}' != data[-1]:
			data += '{' + '}' # I have no idea how to add both of them using just a single string
		self.output += f"{mode}:\n\t{data}\n"

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
	def createMain(self):
		self.output += "\nint main(){\n\n\t" + f"{self.className} obj;\n\tstd::cout << \"Succesfully created {self.className} object!\\n\";\n\tstd::cin.get();\n\treturn 0;\n" + '}'
		self.writeToObject()
	def writeToObject(self):
		f = open(self.fileName, "w")
		f.write(self.output)
		f.close()
		print(f"Wrote to file {self.fileName} having class name {self.className}")

def main():
	fileName = "output" # Output file name goes here. -> Optional to add .cpp as this script would append it anyways.
	className = "check" # Class name goes here

	gen = CPP_GEN(fileName) # Creation of object

	# Attributes that must be added.
	attributes = {
		"char* address" : "private",
		"int age" : "protected",
		"string name" : "public",
		"float cgpa" : "private"
	}
	# Methods that be added.
	'''
	To add methods, you must pass the methods as a dictionary,the key must be a tuple,
	containing the name, return type and visibility mode, respectively. While, the 
	value must be a list containing all arguments. If the function has no arguments,
	just pass an empty list
	'''
	methods = {
		("bool", "hasName", "private") : [],
		("int", "inputAge", "public") : ['int age', 'string name']
	}

	'''
	There's also another way to add methods, you just create a string, add the method
	in there and pass that string to addDirectMethod method along with the visibility mode:
	-> method = 'string updateName(string name){}'
	-> gen.addDirectMethod(method, "public")
	'''

	method = "string capitalize(string data, int out)" # This is just a random method to give you a POC
	mode = "public" # Just a testing variable that is used on line 178
	attribute = "string fatherName" # Testing variable that will be passed to addDirectAttrib method on line 202

	gen.createClass(className)
	gen.addAttrib(attributes)
	gen.addDirectAttrib(attribute, mode) # This method allows direct addition of attributes by passing a string of attribute and a string of visibility mode
	gen.addDirectMethod(method, mode)
	gen.addDirectMethod(data=f"int totalAge(int age, {format(className.capitalize())} obj)", mode="protected") # Adding a method, directly. Just for a POC
	gen.addMethod(methods)
	gen.createObject() # This will generate all the setters, getters and a constructor
if __name__ == "__main__":
	main()
