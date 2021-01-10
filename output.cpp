/* CPP Generator by @TheFlash2k */
#include <iostream>
#include <string>
using namespace std;

class Check{
private:
	char* address;
protected:
	int age;
public:
	string name;
private:
	float cgpa;
public:
	string fatherName
public:
	string capitalize(string data, int out){}
protected:
	int totalAge(int age, Check obj){}
private:
	bool hasName (){}
public:
	int inputAge (int age, string name){}
public:
	Check(char* address , int age , string name = "", float cgpa ): address(address), age(age), name(name), cgpa(cgpa) {}
public:
	void setAddress(char* address){
		this->cgpa = cgpa;
	}
	void setAge(int age){
		this->cgpa = cgpa;
	}
	void setName(string name){
		this->cgpa = cgpa;
	}
	void setCgpa(float cgpa){
		this->cgpa = cgpa;
	}
public:
	char* getAddress() const {
		return this->address;
	}
	int getAge() const {
		return this->age;
	}
	string getName() const {
		return this->name;
	}
	float getCgpa() const {
		return this->cgpa;
	}
};

int main(){

	Check obj;
	std::cout << "Succesfully created Check object!\n";
	std::cin.get();
	return 0;
}
