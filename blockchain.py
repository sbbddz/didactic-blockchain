from time import time
import utils

class Chain():

    def __init__(self):
        self.chain = []
        self.transactions = []

        self.new_block(proof=6969, pre_hash=1)

    def new_block(self, proof, pre_hash=None):

        block = {
            'id': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'proof': proof,
            'pre_hash': pre_hash or utils.hash(self.chain[-1])
        }

        self.transations = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, receiver, amount):
        self.transactions.append(
            {
                'sender': sender,
                'receiver': receiver,
                'amount': amount
            }
        )

        return self.last_block['id'] + 1

    def proof(self, last):
        proof = 0
        while utils.validate_proof(last, proof) is False:
            proof += 1

        return proof

    @property
    def last_block(self):
        return self.chain[-1]
