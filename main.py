from blockchainFiles.hashing import create_hash
from blockchainFiles.block import Block
from random import randrange


def create_random_transactions():
    num_of_transactions = randrange(0, 10, 1)
    transactions = []
    var = 0
    while var < num_of_transactions:
        transactions.append(create_hash())
        var += 1
    return transactions


def print_block(block):
    # block height
    print("block height****")
    print(block.block_height)
    print(".")

    # transactions in block
    print("transactions in block****")
    for x in block.input_transactions:
        print(x)
    print(".")

    # magic number
    print("magic number****")
    print(block.magic_no)
    print(".")

    # number of transaction
    print("number of transaction****")
    print(block.num_of_transactions)
    print(".")

    # ----block header

    # version
    print("block version")
    print(block.block_header.block_version)
    print(".")

    # hash prev block
    print("previous hash block")
    print(block.block_header.hash_prev_block)
    print(".")

    # hash merkle tree
    print("merkle hash root")
    print(block.block_header.hash_merkle_root)
    print(".")

    # hash prev block
    print("time stamp")
    print(block.block_header.time_stamp)
    print(".")

    # target
    print("target")
    print(block.block_header.target)
    print(".")

    # nonce
    print("nonce")
    print(block.block_header.nonce)


def main():
    # random_block = Block(block_height, hash_prev_block, input_transactions)
    random_block = Block("none, fix it", 'None, fix it', create_random_transactions())
    print_block(random_block)


if __name__ == '__main__':
    main()
