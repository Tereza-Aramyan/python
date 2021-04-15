'''
Password generator, the passwords must have
  * At least 8 characters.
  * Both uppercase and lowercase letters.
  * Contains letters and numbers.
  * Contains at least one special character, e.g., ! @ # ? ] , do not contains < or > in password

'''


import string
import itertools

all_char = f'{string.digits}{string.punctuation}{string.ascii_letters}'
k = itertools.count(0)

def contains_num(generated_num):
    return any(str(el).isdigit() for el in generated_num)

def contains_up(generated_num):
    return any(el.isupper() for el in generated_num)

def contains_low(generated_num):
    return any(el.islower() for el in generated_num)

def contains_pun(generated_num):
    return any(str(el) in string.punctuation for el in generated_num)


def generator_random(len_char):

    while True:

        generated_tuple = tuple(itertools.product(all_char , repeat=len_char ))
        generated_number =generated_tuple[next(k)]

        while (not (contains_num(generated_number) &  contains_pun(generated_number) &  contains_up(generated_number) & contains_low(generated_number)) ):
            generated_number = generated_tuple[next(k)]
        yield(generated_number)



gen = generator_random(4)
print(next(gen))
print(next(gen))
print(next(gen))