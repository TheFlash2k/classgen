# ClassGen - A Python3 based script to generate CPP files for custom classes.

##### Usage:
Changes within the code is required:
Check `main()` function
```
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
```

##### fileName - Change it to the filename you want to store it in
##### className -> The Class that you want to generate
##### Attributes -> This is a dictionary that will take all the attributes. The key would be the field along with it's cpp data type and the value would be it's visibility mode.

#### Features to be added:
> Methods:
A capability to add custom methods along with their parameters would be added soon.


Why I made this script:
During my exams, I really waste my time writing each setter, getter, constructor and stuff. I was free today and wanted more stuff on my github so decided to write this idk. ;-;
