# Puzzle 8

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
[0b]	PUSH1	00
[0d]	DUP1	
[0e]	DUP1	
[0f]	DUP1	
[10]	DUP1	
[11]	SWAP5	
[12]	GAS	
[13]	CALL	
[14]	PUSH1	00
[16]	EQ	
[17]	PUSH1	1B
[19]	JUMPI	
[1a]	REVERT	
[1b]	JUMPDEST	
[1c]	STOP
```
Hex: `36600080373660006000F0600080808080945AF1600014601B57FD5B00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x6001600c60003960016000F3FD`

## Explanation

Similar to [puzzle 7](puzzle_7.md), this puzzle requires to send init code which will deploy a contract. The endgame is quite different here though as the next instructions (from `0xb` to `0x13`) sets up a call to our contract's code.

The return value from the call is then checked and if equal to zero, the puzzle will be solved ! Looking at the [`CALL`](https://www.evm.codes/#f1) documentation, we can see it returns 0 if the called sub-context reverts.

Hence, the calldata required to deploy a contract that reverts can be described as :
```
[00]	PUSH1	01	# Size of the actual code that will be deployed
[02]	PUSH1	0c  # Location of the code within the current context (corresponds here to SELFBALANCE instruction)
[04]	PUSH1	00  # Memory address to store the code
[06]	CODECOPY	# Stores the code in memory
[07]	PUSH1	01	# Size of the actual code that will be deployed
[09]	PUSH1	00	# Memory address to store the code
[0b]	RETURN		# Return the address and size to the 'CREATE' context code
[0c]	REVERT # Code that will be deployed, revert will make the 'CALL' return 0 which is expected to solve the puzzle
```
Hex: `0x6001600c60003960016000F3FD`

*Note: instead of simply using the `REVERT` opcode, it's possible to revert the sub-context through more creative ways such as missing or passing illegal arguments to opcodes, using all the gas, overflowing the stack, illegal jumps, etc.* 