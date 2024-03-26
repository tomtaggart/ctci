#include <string>

#include "str_1_1_DupSol2.h"

using namespace std;

 
bool str_1_1_DupSol2::findIn(string s) {
    for (int i=0; i < s.length() - 1; i++) {
        for (int j = i + 1; j < s.length(); j++) {
            if (s.at(i) == s.at(j)) {
                return true;
            }
        }
    }
return false;
}