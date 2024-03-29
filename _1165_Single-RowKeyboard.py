# There is a special keyboard with all keys in a single row.

# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

 

# Example 1:

# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4. 
# Example 2:

# Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
# Output: 73
 

# Constraints:

# keyboard.length == 26
# keyboard contains each English lowercase letter exactly once in some order.
# 1 <= word.length <= 10^4
# word[i] is an English lowercase letter.

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        mov = prv = 0
        for c in word:
            idx = keyboard.find(c)
            mov += abs(idx - prv)
            prv = idx
        return mov

"""
However note that the above solution is not optimal, the problem is that the
keyboard.find is O(length of `keyboard`), so we can use some data structures to
store the position per character. Below solution uses a hashmap, this can also
be done using an array. We can just map the index of 'a' to the first element,
the index of 'b' to the second element, the index of 'c' to the third element
and so on.
"""
class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        mov = prv = 0
        idxs = {}
        for i in range(len(keyboard)):
            idxs[keyboard[i]] = i
        for c in word:
            idx = idxs[c]
            mov += abs(idx - prv)
            prv = idx
        return mov
