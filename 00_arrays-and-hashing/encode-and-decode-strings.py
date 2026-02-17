"""
Encode the string by putting the number of digits, followed by a delimiter character like '#', then the string. When decoding, you can then get the number of digits by looping over the string until the delimiter is reached -> this is the number of digits as a string -> convert to int -> skip over the delimiter -> loop through the string numDigits times to get that word
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        words = []
        for word in strs:
            words.append(f'{len(word)}#word')
        
        # joining once at the end for performance, since += would
        # recreate a new string every time, since strings are immutable.
        return "".join(words)

    def decode(self, s: str) -> List[str]:
        cur_index = 0
        words = []

        # DEBUG: s = "4#neet4#code4#love3#you"
        while cur_index < len(s):
            # 1. get the number before '#' (which separates)
            # the number from the word itself
            letter_count_str = ""
            while s[cur_index] != '#':
                # this means we're still getting the letter_count
                letter_count_str += (s[cur_index]) # DEBUG: 4 (string)
                cur_index += 1
            letter_count = int(letter_count_str) # DEBUG: 4 (int)

            # 2. get the word after the #, which I'll know 
            # when to stop looking for, based on the letter_count

            # Now, we should be at the '#' delimiter, so to skip:
            cur_index += 1

            word = ""
            # Now, we're at the word
            for i in range(letter_count): # DEBUG: 0, 3
                # for as many times as letter_count, we add the char
                # to our word
                word += (s[cur_index])
                cur_index += 1

            words.append(word)
            # 3. Move onto the next word once letter_count reached
            # when looking for the word 
        return words
