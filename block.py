import hashlib
from random import random, seed, randrange
import time


class Block:
    def __init__(self, next_block, prev_block, block_height, hash_prev_block, input_transactions):
        self.block_hash = 123
        self.next_block = next_block
        self.prev_block = prev_block
        self.magic_no = "0xD9B4BEF9"
        self.block_height = block_height
        self.num_of_transactions = len(input_transactions)
        self.input_transactions = input_transactions
        # Blockhead------------------------------
        self.block_version = get_version()
        # TODO: hash_prev_block
        self.hash_prev_block = hash_prev_block
        self.hash_merkle_root = get_hash_merkle_root(input_transactions)
        self.time_stamp = get_time_stamp()
        # TODO: target
        self.target = get_target(block_height, get_time_stamp())
        # TODO: nonce
        self.nonce = None


def get_hash_merkle_root(transactions):
    hash_ = None
    tx = transactions.copy()
    if len(tx) == 0:
        return []
    temp = []
    while len(tx) > 1:
        concat = tx[len(tx)-1] + tx[len(tx)-2]
        curr_hash = hashlib.sha256(concat.encode('utf-8')).hexdigest()
        temp.append(curr_hash)
        del tx[len(tx) - 1]
        del tx[len(tx) - 1]
    if len(tx) == 1:
        tx.append(tx[0])
        concat = tx[0] + tx[1]
        curr_hash = hashlib.sha256(concat.encode('utf-8')).hexdigest()
        temp.append(curr_hash)
        del tx[len(tx) - 1]
        del tx[len(tx) - 1]
    if len(temp) == 1:
        return temp[0]
    else:
        hash_ = get_hash_merkle_root(temp)
        return hash_


def get_version():
    versions = ['0x20400000', '0x20000000', '0x20c00000', '0x20e00000', '0x20800000', '0x3fffe000', '0x3fff0000',
                '0x37ffe000', '0x20384000', '0x20600000',
                '0x27ffe000']
    return versions[randrange(0, 10, 1)]


def get_time_stamp():
    return int(time.time())


def get_target(block_height, time_stamp):
   return None







