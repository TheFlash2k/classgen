#!/usr/bin/env python3
'''
This will generate a cpp having class of name, whatever you name it.
AUTHOR: TheFlash2k
Github Link: https://github.com/TheFlash2k/
Written in: Python3
'''
class CPP_GEN:
	banner = "/* CPP Generator by @TheFlash2k */"
	output = ""
	libraries = ["iostream", "string"]
	namespaces = []

	def __init__(self, fileName):

		''' Setting up the specified libraries '''

		self.attributes = list()
		self.setFileName(fileName)
		self.prevMode = "" # Will contain the visibility mode of the last attribute
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

	def addFriend(self, className):
		mode = "public"
		if self.prevMode != mode:
			self.output += f"{mode}:\n"
			self.prevMode = mode
		self.output += f"\tfriend class {className};\n"

	def addLibrary(self, library):
		if type(library) == str:
			self.libraries.append(library)
		elif type(library) == list:
			for lib in library:
				self.libraries.append(lib)

	def addNamespace(self, namespace):
		if type(namespace) == str:
			self.namespaces.append(namespace)
		elif type(namespace) == list:
			for ns in namespace:
				self.namespaces.append(ns)

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
			if self.prevMode == mode:
				self.output += f"\t{field};\n"
			else:
				self.output += f"{mode}:\n\t{field};\n"
				self.prevMode = mode
			self.prevMode = mode
		self.hasAttribs = True
	def addDirectAttrib(self, data, mode):
		if self.prevMode == mode:
			self.output += f"\t{data}\n"
		else:
			self.output += f"{mode}:\n\t{data}\n"
		self.prevMode = mode
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
			if self.prevMode == mode:
				self.output += f"\t{rtType} {name} {args}\n"
			else:
				self.output += f"{mode}:\n\t{rtType} {name} {args}\n"
				self.prevMode = mode

	def addDirectMethod(self, data, mode):
		if '{' != data[-2] and '}' != data[-1]:
			data += '{' + '}' # I have no idea how to add both of them using just a single string
		if self.prevMode == mode:
			self.output += f"\t{data}\n"
		else:
			self.output += f"{mode}:\n\t{data}\n"
		self.prevMode = mode

	def validate(self, cons):
		numbers = ('int', 'float', 'double', 'long', 'short')
		for number in numbers:
			if number in cons:
				cons += " = 0"
		if "string" in cons:
			if "*" in cons:
				cons += " = NULL"
			else:
				cons += " = {}"
		elif "char" in cons:
			if "*" in cons:
				cons += " = \"\""
			else:
				cons += " = '_'"
		elif "*" in cons:
			cons += " = NULL"
		elif "[" in cons and "]" in cons:
			cons += " = { 0 " + "}"
		return cons

	def generateConstructor(self):
		mode = "public:\n\t" if self.prevMode != "public" else "\t"
		tAttribs = len(self.attributes)
		index  = 0
		cons = f"{self.className}("
		attribs = list()
		for i in range(tAttribs):
			attribs.append(self.validate(self.attributes[index]))
			index += 1
		attribs = ', '.join(attribs)
		cons += attribs + ") : "
		attributes = ""
		for data in self.attributes:
			data = data.split()[1]
			cons += f"{data}({data}), "
		cons = cons[:-2] # Removing the extra comma.
		cons += " {}\n"
		self.output += mode + cons
		self.prevMode = "public" # Setting the mode to be public
	# This will create the setters and getter methods

	def generateSetters(self):
		variables = self.attributes
		vars = list()
		setters = list()
		
		for variable in variables:
			vars.append(variable.split()[1])
		variables_list = list()
		for var in vars:
			setters.append(f"\tvoid set{var.capitalize()}(")
			variables_list.append(var)
		it = 0
		for i in range(len(self.attributes)):
			setters[i] += self.attributes[i] + "){"
			setters[i] += f"\n\t\tthis->{variables_list[it]} = {variables_list[it]};"
			self.output += setters[i] + "\n\t}\n"
			it += 1
	def generateGetters(self):
		variables = self.attributes
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
		## Adding the libraries:
		inc = "#include "
		_namespace = "using namespace "

		libs = [f"{inc}<{i}>" for i in self.libraries]
		nss = [f"{_namespace}{i};" for i in self.namespaces]

		self.output = self.banner + "\n" + "\n".join(libs) + "\n\n" + "\n".join(nss) + "\n\n" + self.output
		self.writeToObject()

	def writeToObject(self):
		f = open(self.fileName, "w")
		f.write(self.output)
		f.close()
		print(f"Wrote to file {self.fileName} having class name {self.className}")