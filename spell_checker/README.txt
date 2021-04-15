Spell-checker

    utils.py :
     1. Counts  two strings Levenshtein distance.
     2. Counts Soundex code for string

    checker.py :
     1. maps Soundex code to words of dictionary.txt file
     2. get misspelled word, count Soundex code, get list of words that has the same Soundex code as misspelled word,
        count Levenstein distance between misspelled word and that list of words and return words that have minimal Levenstein distance with misspelled word.


When you run main.py this will be printed:

Exp1: Choose from options:
1. Levenshtein
2. Soundex
Type 1, 2 or 3: 1
First string: kitten
Seccond string: sitting
Levenshtein distance for "kitten" and "sitting" is 3

Exp2: Choose from options:
1. Levenshtein
2. Soundex
Type 1, 2 or 3: 2
Input string: example
Soundex code for "example" is E251

Exp.: Choose from options:
1. Levenshtein
2. Soundex
3. Spell correction
Type 1, 2 or 3: 3
Write misspelled word: sprinq
Possible options: spring, sprint