from random import random, seed, randrange
import time


class Block_header:
    def __init__(self, hash_prev_block, hash_merkle_root, target, nonce):
        # TODO: block_version
        self.block_version = get_version()
        # TODO: hash_prev_block
        self.hash_prev_block = hash_prev_block
        # TODO: hash_merkle_root
        self.hash_merkle_root = hash_merkle_root
        # TODO: time_stamp
        self.time_stamp = get_time_stamp()
        # TODO: target
        self.target = target
        # TODO: nonce
        self.nonce = nonce


def get_version():
   # versions = ['0x20400000', '0x20000000', '0x20c00000', '0x20e00000', '0x20800000', '0x3fffe000', '0x3fff0000',
               # '0x37ffe000', '0x20384000', '0x20600000',
               # '0x27ffe000']
   # return versions[randrange(0, 10, 1)]
   return "none, fix it"


def get_time_stamp():
    return int(time.time())
