from classgen import CPP_GEN

def main():
	fileName = "output" # Output file name goes here. -> Optional to add .cpp as this script would append it anyways.
	className = "Admin" # Class name goes here

	generator = CPP_GEN(fileName)

	attributes = {
		"std::string userName" : "private",
		"uint_t UID" : "public",
		"std::vector<std::string> posts" : "private"
	}

	methods = { ("std::map<int, std::string>", "uid", "public") : ['int key', 'std::string possible_value=""'] }
	libraries = [ "vector", "map" ]
	namespaces = [ "std" ]

	generator.createClass(className)
	generator.addAttrib(attributes)
	generator.addMethod(methods)
	generator.addLibrary(libraries)
	generator.addNamespace(namespaces)

	generator.createObject()

if __name__ == "__main__":
	main()
