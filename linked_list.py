"""
THE BLOCKCHAIN IS A DATA STRUCTURE ON ITS OWN WHICH IS AN IMPROVED VERSION OF THE LINKED LIST
So here I am just going to implement the linked list and then I will create a seperate file which turn it to a blockchain
"""

class Block:
    def __init__(self):
        self.next_block = None
        self.data = None

block_A = Block()
block_B = Block()
block_C = Block()




block_A.next_block = block_B
block_A.data = 56

block_B.next_block = block_C
block_B.data = "Cookies"

block_C.next_block = None
block_C.data = 897756

current_block = block_A
while current_block != None:
    print("Data: ",end = '')
    print(current_block.data)
    current_block = current_block.next_block