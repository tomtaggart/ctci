#include <string>
#include <unordered_map>

#include "str_1_2_Perm.h"

using namespace std;

 
bool str_1_2_Perm::permutations(std::string s1, std::string s2) {
    if (s1.length() != s2.length()) {
            return false;
        }

        unordered_map<char, int> charDB;
		// Fill hashmap with s1 char counts
        for (int i=0; i < s1.length(); i++) {
			if (charDB.find(s1.at(i)) == charDB.end()) {
				charDB[s1.at(i)] = 1;
			}
			else {
				charDB[s1.at(i)] += 1;  //TODO: works?
			}
		}

        // Parse s2
        for (int i=0; i < s2.length(); i++) {
            if (charDB.find(s2.at(i)) == charDB.end()) {
                return false;
            }
            else {
                if (charDB.find(s2.at(i))->second == 0) {
                    return false;
                }
                else {
                    charDB[s2.at(i)] -= 1; //TODO: works?
                }
            }
        }
		return true;
}