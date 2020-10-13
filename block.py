from blockchainFiles.block_header import Block_header
import hashlib


class Block:
    def __init__(self, block_height, hash_prev_block, input_transactions):
        self.magic_no = "0xD9B4BEF9"
        self.block_height = block_height
        self.num_of_transactions = len(input_transactions)
        self.input_transactions = input_transactions
        # Block_header(hash_prev_block, hash_merkle_root, target, nonce)
        self.block_header = Block_header(hash_prev_block, get_hash_merkle_root(input_transactions), "none, fix it", "None, fix it")


def get_hash_merkle_root(transactions):
    # TODO need sha256 hash
    tx = transactions.copy()
    if tx == 0:
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
        get_hash_merkle_root(temp)







