
from operator import itemgetter

def levenshtein(word1, word2):
    word1 = f" {word1}"
    word2 = f" {word2}"
    for i in range(len(word1)):
        line = []
        for j in range(len(word2)):
            if( i == 0 or j == 0):
                line.append(abs(i-j))
            else:
                a = 0 if word1[i] == word2[j] else 1
                min_list =[last_line[j] + 1, line[j-1] + 1, last_line[j-1] + a]
                line.append(min(min_list))
        last_line = tuple(line)
    return itemgetter(-1)(last_line)

def second_func(a,i):
    my_tuple = (("HW"), ("BFPV"),
                ("CGJKQSXZ"), ("DT"),
                ("L"), ("MN"), ("R"))
    for j in range(len(my_tuple)) :
        if (a[i].upper() in my_tuple[j]):
            return j

def soundex(a):
    out_string = a[0].upper()
    for i in range(1, len(a)-1):
            if (second_func(a,i) is not None):
                out_string = f"{out_string}{second_func(a,i)}"
                if (second_func(a,i) == second_func(a,i+1)) :
                    i += 1
                if (len(out_string) == 4):
                    break
    while(len(out_string) < 4):
        out_string = f"{out_string}0"
    return out_string









