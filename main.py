import hashlib
import json
import utils
from time import time
from textwrap import dedent
from uuid import uuid4
from flask import Flask, jsonify, request
from blockchain import Chain

app = Flask(__name__)
node_id = str(uuid4()).replace('-', '')
blockchain = Chain()

@app.route('/chain/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof(last_proof)

    blockchain.new_transaction(sender="1", receiver=node_id, amount=1)
    pre_hash = utils.hash(last_block)
    block = blockchain.new_block(proof, pre_hash)

    response = {
            'message': 'Forged new Block',
            'index': block['id'],
            'transactions': block['transactions'],
            'pre_hash': block['pre_hash']
    }

    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def chain():
    return jsonify({
            'chain': blockchain.chain
        }), 200

@app.route('/transation/new', methods=['POST'])
def new_transation():
    data = request.get_json()
    print(data)
    required = ['sender', 'recipient', 'amount']
    
    if (len(data) != len(required) or list(data.keys()) != list(required)):
        print(data)
        return 'Missing', 400

    index = chain.new_transaction(data['sender'], data['recipient'], data['amount'])
    response = {'message': f'Transaction added to block {index}'}
    return jsonify(response), 201


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
