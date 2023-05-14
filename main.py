import hashlib

class Block:
    def __init__(self, previous_block_hash, transactions):
        self.previous_block_hash = previous_block_hash
        self.transactions = transactions

        self.block_data = f"{' '.join(transactions)}:{previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()
    
    def generate_genesis_block(self):
        self.chain.append(Block('0', []))
    
    def create_tx_block(self, transactions):
        block_height = len(self.chain)
        prev_block = self.chain[block_height-1]
        previous_block_hash = prev_block.block_hash
        self.chain.append(Block(previous_block_hash, transactions))
    
    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")



# txns
t1 = "Alice sends 1 BTC to Bob."
t2 = "Cliff send 0.5 BTC to Dave."
t3 = "Bob sends 0.2 BTC to Dave."
t4 = "Eva sends 0.5 BTC to Alice."

myBlockchain = Blockchain()

myBlockchain.create_tx_block([t1,t2])
myBlockchain.display_chain()

myBlockchain.create_tx_block([t3,t4])
myBlockchain.display_chain()