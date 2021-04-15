from utils import soundex,levenshtein


def mapping(in_sandex):
    my_dict = {}
    f = open('dictionary.txt')
    while True:
        line = (f.readline()).replace('\n', '')
        if not line:
            break
        if ( (line[0].upper() == in_sandex[0])):
            if (soundex(line)==in_sandex):
               my_dict[line] = soundex(line)
    f.close()
    return my_dict


def spell_correction(misspelled_word: str):
    my_dict = mapping(soundex(misspelled_word))
    for k in my_dict.keys():
        my_dict[k] = levenshtein(misspelled_word,k)

    sorted_values = sorted(my_dict.values())
    out = ''

    for i in my_dict.keys():
        if(my_dict[i] == sorted_values[0]):
            out = f'{out},{i}'

    return(out[1:])
