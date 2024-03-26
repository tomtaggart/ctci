/*
 * Problem 1.1
 * Implement an algorithm to determine if a string has all unique characters.
 * What if you cannot use additional structures?
 *
 * Solution 2
 * This solution checks for duplicates in place. See the 
 * /mathproofs/MATHPROOF.pdf file for an explanation of how, and proof that, 
 * the algorithm works. This solution has a time complexity of O(n^2) and a
 * space complexity of O(1).
 *
 * 
 * Solution 3
 * This solution is similar to solution 1. The difference is that solution 3
 * validates the size of the character set, C, and creates an array of size C that
 * holds boolean values initialized to false. The index of the array is the
 * character number. When a character is first found the boolean for that character
 * is set to true. If a character is found a second time, the boolean for the
 * character in the array will be true; thus detecting a duplicate. You can as well
 * reject any string longer than the character set as containing duplicates. This
 * improves the space complexity of solution 1 to O(1). I have not implemented this
 * solution as it only makes sense for an ASCII character set. A unicode character
 * set would complicate this and arguably would most likely be no better than
 * solution 1.
 */

package ctci;

public class str_1_1_DupSol2 implements Duplicates {  
    public static Boolean findIn(String s) {
		for (int i=0; i < s.length() - 1; i++) {
			for (int j = i + 1; j < s.length(); j++) {
				if (s.charAt(i) == s.charAt(j)) {
					return true;
				}
			}
		}
		return false;
	}
}