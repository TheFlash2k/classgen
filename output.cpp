/* CPP Generator by @TheFlash2k */
#include <iostream>
#include <string>
using namespace std;

class Check{
private:
	char* address;
	float cgpa;
protected:
	int age;
public:
	string name;
	string fatherName
	string capitalize(string data, int out){}
private:
	int totalAge(int age, Check obj){}
public:
	bool hasName (){}
	int inputAge (int age, string name){}
	Check(char* address = "", float cgpa = 0, int age = 0, string name = "") : address(address), cgpa(cgpa), age(age), name(name) {}
	void setAddress(char* address){
		this->name = name;
	}
	void setCgpa(float cgpa){
		this->name = name;
	}
	void setAge(int age){
		this->name = name;
	}
	void setName(string name){
		this->name = name;
	}
	char* getAddress() const {
		return this->address;
	}
	float getCgpa() const {
		return this->cgpa;
	}
	int getAge() const {
		return this->age;
	}
	string getName() const {
		return this->name;
	}
};

int main(){

	Check obj;
	std::cout << "Succesfully created Check object!\n";
	std::cin.get();
	return 0;
}
