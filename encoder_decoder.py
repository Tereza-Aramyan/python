'''
Binary-string-encoder-and-decoder

  * "encode" function must take plain string as an argument and return binary representaion of the string,
  * "decode" function must take binary representaion of a string as an argument and return decoded string,
  * input for the decode and output of encode function must contain only '0's and '1's,
  * the plain string may contain latin letters, numbers, space and other characters,
'''
import re

def decode(expression):
    return ''.join([chr(int(i, 2)) for i in (re.findall('[0,1]{8}', expression)) ])


def encode(expression):
    return ''.join([format(ord(i), '08b') for i in expression])



if __name__ == '__main__':
    plain_str = input("type your plain string : ")
    print(encode(plain_str))
    print(decode(encode(plain_str)))