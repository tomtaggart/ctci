#include <string>
#include <unordered_map>

#include "str_1_1_DupSol1.h"

using namespace std;


bool str_1_1_DupSol1::findIn(string s) {
    unordered_map<char, bool> char_db;
    for (int i=0; i < s.length(); i++) {
        if (char_db.find(s.at(i)) != char_db.end()) {
            return true;
        }
        else {
            char_db[s.at(i)] = true;
        }
    }
    return false;
}