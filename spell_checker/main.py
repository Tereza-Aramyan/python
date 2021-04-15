from utils import levenshtein,soundex
from checker import spell_correction

answer = int(input("Choose from options: \n   1. Levenshtein \n   2. Soundex \n   3. Spell correction \nType 1, 2 or 3: "))
if (answer == 1):
    in1 = input("First string: ")
    in2 = input("Second string: ")
    print (f"Levenshtein distance for \"{in1}\" and \"{in2}\" is {levenshtein(in1,in2)}")
elif(answer == 2):
    in_string = input ("Input string: ")
    print(f"Soundex code for \"{in_string}\" is {soundex(in_string)}")
elif(answer ==3 ):
    in_string = input ("Write misspelled word: ")
    print(f"Possible options: {spell_correction(in_string)}")
