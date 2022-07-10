# Puzzle 7

### Program

```
[00]	CALLDATASIZE	
[01]	PUSH1	00
[03]	DUP1	
[04]	CALLDATACOPY	
[05]	CALLDATASIZE	
[06]	PUSH1	00
[08]	PUSH1	00
[0a]	CREATE	
[0b]	EXTCODESIZE	
[0c]	PUSH1	01
[0e]	EQ	
[0f]	PUSH1	13
[11]	JUMPI	
[12]	REVERT	
[13]	JUMPDEST	
[14]	STOP
```
Hex: `36600080373660006000F03B600114601357FD5B00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x6001600c60003960016000F347`

## Explanation

A more challenging puzzle for sure ! It requires to understand how contract creation work in the Ethereum blockchain at the low-level :
1. When a call is made to the [`CREATE`](https://www.evm.codes/#f0) instruction, the context in which the code is executing changes.
2. Code specified by the parameters (namely the memory address, offset and size of where the code is located) of the call to `CREATE` is then executed in this context. This running code is known as the initialization code of the contract.
3. `CREATE` then expects the running context to return the memory address and size of where the *actual* contract code can be found.

Hence, the calldata that is provided must satisfy the flow required for contract creation. Here is a breakdown of how the solution achieves this :
```
[00]	PUSH1	01	# Size of the actual code that will be deployed
[02]	PUSH1	0c  # Location of the code within the current context (corresponds here to SELFBALANCE instruction)
[04]	PUSH1	00  # Memory address to store the code
[06]	CODECOPY	# Stores the code in memory
[07]	PUSH1	01	# Size of the actual code that will be deployed
[09]	PUSH1	00	# Memory address to store the code
[0b]	RETURN		# Return the address and size to the 'CREATE' context code
[0c]	SELFBALANCE # Code that will be deployed, a single-byte instruction
```
Hex: `0x6001600c60003960016000F347`

To actually solve the puzzle, the deployed contract code must be of 1 byte size (meaning a 1-byte instruction, any will do). This is verified by the call to [`EXTCODESIZE`](https://www.evm.codes/#3b) opcode to retrieve the deployed code size. 

*Note: This opcode is also often used to differentiate between a Externally Owned Account (EOA, a simple address) and a Contract Account as EOA have a code size of 0 (however this is also true for contract not yet deployed i.e. code executed in the `constructor()` function in Solidity, see [here](https://stackoverflow.com/a/54056854) for more info).*

*PS: A great in-depth analysis of the general init code for Solidity-compiled smart contracts can be found [here](https://leftasexercise.com/2021/09/05/a-deep-dive-into-solidity-contract-creation-and-the-init-code/)*