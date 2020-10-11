from random import randrange, random, seed
from hashlib import sha256

hash_character = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
                  , 'v', 'w', 'x', 'y', 'z']


def create_hash():
    new_hash = "0x"
    i = 0
    while i < 64:
        new_hash += hash_character[randrange(0, 35, 1)]
        i += 1

    return new_hash
