/* CPP Generator by @TheFlash2k */
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

class Admin{
private:
	std::string userName;
public:
	uint_t UID;
private:
	std::vector<std::string> posts;
public:
	std::map<int, std::string> uid (int key, std::string possible_value=""){}
	Admin(std::string userName = {}, uint_t UID = 0, std::vector<std::string> posts = {}) : userName(userName), UID(UID), posts(posts) {}
	void setUsername(std::string userName){
		this->userName = userName;
	}
	void setUid(uint_t UID){
		this->UID = UID;
	}
	void setPosts(std::vector<std::string> posts){
		this->posts = posts;
	}
	std::string getUsername() const {
		return this->userName;
	}
	uint_t getUid() const {
		return this->UID;
	}
	std::vector<std::string> getPosts() const {
		return this->posts;
	}
};

int main(){

	Admin obj;
	std::cout << "Succesfully created Admin object!\n";
	std::cin.get();
	return 0;
}