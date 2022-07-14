import sha3
import binascii

# Functions taken from the great article series of @hayeah on the EVM machine
# See https://medium.com/@hayeah/diving-into-the-ethereum-vm-the-hidden-costs-of-arrays-28e119f04a9b

# Convert a number to 32 bytes array.
def bytes32(i):
    return binascii.unhexlify('%064x' % i)

# Calculate the keccak256 hash of a 32 bytes array.
def keccak256(x):
    return sha3.keccak_256(x).hexdigest()

TRIES = 10**4

# Find a hash that starts with the expected value 'a8'
for i in range(TRIES):
	if (keccak256(bytes32(i))[:2].lower() == 'a8'):
		print(f'[*] Found solution: {i}')
		break