#include <iostream>
#include "str_1_1_DupSol1.h"
#include "str_1_1_DupSol2.h"

using namespace std;


int main() {
    string u = "abcdefghijklmnopqrstuvwxyzSTNHLGDA12345";
    string d = "abcdefghijklmnopqrstuvwxyzSTNHLGDA1234a";
    
    str_1_1_DupSol1::findIn(u);
    str_1_1_DupSol2::findIn(u);
    str_1_1_DupSol1::findIn(d);
    str_1_1_DupSol2::findIn(d);
    return 0;
}