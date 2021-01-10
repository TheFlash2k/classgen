# ClassGen - A Python3 based script to generate CPP files for custom classes.

- What is output.cpp
```
Output.cpp is the file that will be generated when you simply clone the git and run the program. It has been added so that you can see how the output will look like once stored
```

### Usage:
Changes within the code is required:
Check `main()` function
- Change the name of output file
```python
fileName = "output" # -> Output should be replaced with the name of the file.
```
- Change the name of class
```python
className = "check" # -> Replace check with class name
```
- Add Methods through dictionary (Sent as arguement to `addMethod()` method which accepts a dictionary of tuple and list as `K:V` pair)
```python
methods = {
	("bool", "hasName", "private") : [],
	("int", "inputAge", "public") : ['int age', 'string name']
}
gen.addMethod(methods)
'''
To add new methods, simply append a comma to the end of the current methods dictionary, and keep on adding
new methods.
'''
```
- Add Methods through strings
There is another way to add attributes, that is by calling `addDirectMethod()` method with two strings, `method` and `mode`. `method` contains the return type and the name of the string as shown in `line 197` in `classgen.py`. Whilst, mode is the visibility. The calling of this function can be seen on `line 203`
```python
mode = "public"
method = "string capitalize(string data, int out)"
# Test Call 1
gen.addDirectMethod(method, mode)
# Test Call 2
gen.addDirectMethod(data=f"int totalAge(int age, {format(className.capitalize())} obj)", mode="protected")
```
- Add Attributes through dictionary (Sent as argument to `addAttrib()` method which accepts a dictionary of `string` as a `K:V` pair):
```python
attributes = {
	"char* address" : "private",
	"int age" : "protected",
	"string name" : "public",
	"float cgpa" : "private"
}
gen.addAttrib(attributes)
'''
The attributes is a dictionary, the key is a string that contains the return type + variable name.
The value on the other hand, is the visbility mode of the specific variable in the class
'''
```
- Add Attributes through strings:
There is another way to add attributes, that is by calling `addDirectAttrib()` method with two strings, `attribute` and `mode`. `attribute` contains the return type and the name of the string as shown in `line 199` in `classgen.py`. Whilst, mode is the visibility. The calling of this function can be seen on `line 203`
```python
mode = "public"
attribute = "string fatherName"
# Test Call 1
gen.addDirectAttrib(attribute, mode)
# Test Call 2
gen.addDirectAttrib("int numberObjects", "private")
```
- Add other classes to be friend of existing class:<br>
We can declare other classes to be friend of the existing class. Like, consider a class Stack, if in `Node`, we declare this class as friend, the cpp declartion would look like:
```cpp
friend class Stack; // This would be in class Node
```
So, in order to make this happen in python, following method was implemented.
```python
friendClassName = "Employees" # This will be passed to the addFriends function to make this class a friend of the existing class
gen.addFriend(friendClassName) # Calling the friend function adder method.
```
The `friendClassName` represents the name of the class that is to be added as friend. While the method call is pretty self-explanatory

### Why I made this script:
During my exams, I wasted alot of my time writing each setter, getter, constructor and stuff. I was free today and wanted more stuff on my github so decided to write this idk. ;-;

<!--
[![carbon.png](https://i.postimg.cc/WphxysSH/carbon.png)](https://postimg.cc/RqxP65k7)
-->
