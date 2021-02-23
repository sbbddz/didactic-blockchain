import hashlib
import json

def validate_proof(last, proof):
    guess = f'{last}{proof}'.encode()
    guessed_hash = hashlib.sha256(guess).hexdigest()
    return guessed_hash[-2:] == "00"

def hash(block):
    parsed_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(parsed_block).hexdigest()

