from blockchainFiles.block_header import Block_header


class Block:
    def __init__(self, block_height, hash_prev_block, input_transactions):
        self.magic_no = "0xD9B4BEF9"
        self.block_height = block_height
        # Block_header(hash_prev_block, hash_merkle_root, target, nonce)
        self.block_header = Block_header(hash_prev_block, "none, fix it", "none, fix it", "None, fix it")
        self.num_of_transactions = len(input_transactions)
        self.input_transactions = input_transactions


def get_hash_merkle_root(transactions):
    # TODO need sha256 hash
    if len(transactions) == 0:
        return []
    temp = []
    while len(transactions) > 1:
        if len(transactions) == 1:
            transactions.append(transactions[0])






