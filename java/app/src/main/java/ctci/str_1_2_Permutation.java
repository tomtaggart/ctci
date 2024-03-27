/*
 * Problem 1.2
 * Given two strings, s1 & s2, define a function that determines whether as2 is
 * a permutation of s1.
 * 
 * Solution 1
 * As a first step you check both string lengths. If the strings are not the
 * same length they are not permutations of one another. If string lengths are
 * equal, the solution utilizes a hash table initialized as empty. The hash
 * table will have a string:int format. As you iterate through s1 if the char is
 * not in the hash table you add the char with a value of 1. If the char is in
 * the hash table, you increment the value of that char +1. You will wind up
 * with a table of unique chars and their occurance count.
 * 
 * 
 * Next you iterate through s2. The following checks are made:
 * - If a char in s2 is not in the hash table, then the char is unique to s2 and
 * the strings are not permutations.
 * - If the char is in the hash table, check the value. If the value is equal to
 * zero, then there are 1 too many of the particular char in s2 and the strings
 * are not permutations.
 * 
 * - if the value is greater than 0, subtract 1 from the value.
 * 
 * Inevitably, iterating s2 will bring all values down to 0.
 * 
 * This solution has a time and space complexity of O(n).
 * 
 * 
 * Solution 2
 * A second solution exists where you can use an array instead of a hashmap in
 * cases where the char set is small, e.g., ASCII. I am not implementing that
 * here as it is trivial to do so and the algoritm would not change.
 */

package ctci;

import java.util.Map;
import java.util.HashMap;

public class str_1_2_Permutation implements Permutation {
    public static Boolean permutations(String s1, String s2) {
		if (s1.length() != s2.length()) {
            return false;
        }

        Map<Character, Integer> charDB = new HashMap<>();
		// Fill hashmap with s1 char counts
        for (int i=0; i < s1.length(); i++) {
			if (charDB.get(s1.charAt(i)) == null) {
				charDB.put(s1.charAt(i), Integer.valueOf(1));
			}
			else {
				charDB.put(s1.charAt(i), new Integer(
                    charDB.get(s1.charAt(i)).intValue() + 1));
			}
		}

        // Parse s2
        for (int i=0; i < s2.length(); i++) {
            if (charDB.get(s2.charAt(i)) == null) {
                return false;
            }
            else {
                if (charDB.get(s2.charAt(i)) == 0) {
                    return false;
                }
                else {
                    charDB.put(s2.charAt(i), new Integer(
                        charDB.get(s2.charAt(i)).intValue() - 1));
                }
            }
        }
		return true;
	}
}
