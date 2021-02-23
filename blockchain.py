from time import time
import utils

class Chain():

    def __init__(self):
        self.chain = []
        self.transations = []

    def new_block(self, proof, pre_hash=None):

        block = {
            'id': len(self.chain) + 1,
            'timestamp': time(),
            'transations': self.transations,
            'proof': proof,
            'pre_hash': pre_hash or utils.hash(self.chain[-1])
        }

        self.transations = []
        self.chain.append(block)
        return block

    def new_transation(self, sender, receiver, amount):
        self.transations.append(
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
        pass
