from blockchainFiles.hashing import create_hash
from blockchainFiles.block import Block
from random import randrange

last_diff_change_block = None
genesis_block = None
global_block_height = None


def find_block_at_height(desired_block_height, global_block_height, genesis_block):
    block = genesis_block
    while block.block_height < global_block_height:
        if block.block_height == desired_block_height:
            return block
        else:
            block = block.next_block
    return genesis_block


def create_random_transactions():
    num_of_transactions = randrange(1, 10, 1)
    transactions = []
    var = 0
    while var < num_of_transactions:
        transactions.append(create_hash())
        var += 1
    return transactions


def create_test_blockchain():
    first_block = Block(None, None, 0, "N/a", create_random_transactions())
    blocks = 1
    last_block = first_block
    while blocks < 10:
        temp = Block(None, last_block, blocks, last_block.hash_prev_block, create_random_transactions())
        last_block.next_block = temp
        last_block = temp
        blocks += 1
    return first_block


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
    print(block.block_version)
    print(".")

    # hash prev block
    print("previous hash block")
    print(block.hash_prev_block)
    print(".")

    # hash merkle tree
    print("merkle hash root")
    print(block.hash_merkle_root)
    print(".")

    # hash prev block
    print("time stamp")
    print(block.time_stamp)
    print(".")

    # target
    print("target")
    print(block.target)
    print(".")

    # nonce
    print("nonce")
    print(block.nonce)


def main():
    curr_block = create_test_blockchain()
    while curr_block.next_block is not None:
        print_block(curr_block)
        print("***")
        print("***")
        print("***")
        print("***")
        curr_block = curr_block.next_block
    print_block(curr_block)


if __name__ == '__main__':
    main()
