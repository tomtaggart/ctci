#include <iostream>
#include "str_1_1_DupSol1.h"
#include "str_1_1_DupSol2.h"
#include "str_1_2_Perm.h"

using namespace std;


int main() {
    string u = "abcdefghijklmnopqrstuvwxyzSTNHLGDA12345";
    string d = "abcdefghijklmnopqrstuvwxyzSTNHLGDA1234a";
    string str_1_2_permutation_s1 = "aaaabbbbcccc";
    string str_1_2_permutation_s2 = "abcabcabcabc";
    string str_1_2_permutation_s3 = "abcdababcabd";
    string str_1_2_permutation_s4 = "aaaaaaaaaaaa";
    string str_1_2_permutation_s5 = "dabc";
    string str_1_2_permutation_s6 = "xyzg";
    
    str_1_1_DupSol1::findIn(u);
    str_1_1_DupSol2::findIn(u);
    str_1_1_DupSol1::findIn(d);
    str_1_1_DupSol2::findIn(d);
    str_1_2_Perm::permutations(str_1_2_permutation_s1, str_1_2_permutation_s2);
    str_1_2_Perm::permutations(str_1_2_permutation_s1, str_1_2_permutation_s3);
    str_1_2_Perm::permutations(str_1_2_permutation_s1, str_1_2_permutation_s4);
    str_1_2_Perm::permutations(str_1_2_permutation_s1, str_1_2_permutation_s5);
    str_1_2_Perm::permutations(str_1_2_permutation_s5, str_1_2_permutation_s6);



    return 0;
}