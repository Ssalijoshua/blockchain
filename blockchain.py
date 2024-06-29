import hashlib
import json

class Block:
    def __init__(self):
        self.next_block = None
        self.data = None
        self.parent_hash = None

block_A = Block()
block_B = Block()
block_C = Block()

block_A.next_block = block_B
block_A.data = 56

block_B.next_block = block_C
block_B.data = "Cookie"
block_B.parent_hash = hashlib.sha384(json.dumps({k: v for k, v in block_A.__dict__.items() if k != "next_block"}).encode('utf-8')).hexdigest()

block_C.next_block = None
block_C.data = 897756
block_C.parent_hash = hashlib.sha384(json.dumps({k: v for k, v in block_B.__dict__.items() if k != "next_block"}).encode('utf-8')).hexdigest()

current_block = block_A
while current_block is not None:
    print("Hash:", current_block.parent_hash)
    current_block = current_block.next_block
