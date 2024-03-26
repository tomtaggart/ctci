/*
 * Problem 1.1
 * Implement an algorithm to determine if a string has all unique characters.
 *
 * Solution 1
 * This solution utilizes a hash table initialized as empty. As you iterate through
 * the string you check the hash table for the char. If the char is in the table
 * it has occured in the string before and you exit the algorithm. If the char is
 * not in the table you add it to the table and move on to the next char in the
 * string for evaluation.
 *
 * This solution has a time and space complexity of O(n).
 */

 package ctci;

import java.util.Map;
import java.util.HashMap;

public class str_1_1_DupSol1 implements Duplicates {	
	public static Boolean findIn(String s) {
        Map<Character, Boolean> charDB = new HashMap<>();
		for (int i=0; i < s.length(); i++) {
			if (charDB.get(s.charAt(i)) != null) {
				return true;
			}
			else {
				charDB.put(s.charAt(i), true);
			}
		}
		return false;
	}
}