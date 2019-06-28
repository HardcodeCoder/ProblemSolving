#  -*- coding: utf-8 -*-
""" 
Created on Friday 28 Jun 2019 16:45:13
 
@author: HardcodeCoder
"""

# About the problem : 
# Program to decode a given sentence (words seperated by space)
# The first word of the sentence will shift its characters backwards 
# by 1 character the second word will shift all its characters by 2 and so on.
# Spaces will not be decoded and will print as it is.
# Upper case characters will decode to upper case characters
# Example : - 
# Input : abc xyz jgk
# Output : zab vwx gdh
# Characters of first word are shifted by -1 characters : a -> z, b -> a, c -> b 
# Characters of secons word are shifted by -2 characters : x -> v, y -> w, z -> x.

def decode(word, shift):
    decoded_word = ""
    for i in word:
        asc = ord(i)
        if asc - shift < 65 :
            dec_asci = 91 - (65 - (asc - shift))
        elif asc >= 97 and asc <= 122 and asc - shift < 97 :
            dec_asci = 123 - (97 - (asc - shift))
        else:
            dec_asci = asc - shift
        decoded_char = chr(dec_asci)
        decoded_word = decoded_word + decoded_char
    return decoded_word

print("Enter the encoded string : ",end = "")
word_str = str(input())
word_str = word_str + " "
shift = 1
word = ""
for i in word_str:
    if i != ' ':
        word = word + i
    else:
        print(decode(word, shift), end=" ")
        shift+=1
        word = ""

