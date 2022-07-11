# Puzzle 3

### Program

```
[00]	CALLDATASIZE	
[01]	PUSH1	00
[03]	PUSH1	00
[05]	CALLDATACOPY	
[06]	CALLDATASIZE	
[07]	PUSH1	00
[09]	PUSH1	00
[0b]	CREATE	
[0c]	PUSH1	00
[0e]	DUP1	
[0f]	DUP1	
[10]	DUP1	
[11]	SWAP4	
[12]	GAS	
[13]	DELEGATECALL	
[14]	PUSH1	05
[16]	SLOAD	
[17]	PUSH1	aa
[19]	EQ	
[1a]	PUSH1	1e
[1c]	JUMPI	
[1d]	INVALID	
[1e]	JUMPDEST	
[1f]	STOP
```
Hex: `3660006000373660006000F06000808080935AF460055460aa14601e57fe5b00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x6005600c60003960056000F360aa600555`

## Explanation

Instead of the traditional [`CALL`](https://www.evm.codes/#f1), this puzzle uses a very interesting feature of the EVM, the [`DELEGATECALL`](https://www.evm.codes/#f4).

This allows for the called context to access the storage of the callee and potentially modifiy it, enabling for elaborated designs such as [proxy contracts]() which allows to separate the logic code from the storage.

In this case, the puzzle will look for the value stored at the storage offset `0x5` and check that it equals `0xaa` to successfully execute the `JUMPI` instruction.

Hence, the deployed code can use the shared storage offered by the `DELEGATECALL` to store this value :
```
[00]	PUSH1	05  # Size of deployed contract code
[02]	PUSH1	0c  # Offset from which the deployed contract starts in this context 
[04]	PUSH1	00	# Memory location to store deployed contract
[06]	CODECOPY    # Copy the contract code to memory
[07]	PUSH1	05  # Size of deployed contract code
[09]	PUSH1	00  # Memory location of deployed contract
[0b]	RETURN	    # Return to calling context (return from CREATE)
[0c]	PUSH1	aa  # Value to put in storage
[0e]	PUSH1	05  # Storage key
[10]	SSTORE      # The callee storage will be modified through this instruction
```

This will set the appropriate value for the `SLOAD` instruction and solve the puzzle !

*Note: `DELEGATECALL` is a very powerful but potentially dangerous feature of EVM smart contracts. Since the storage of the callee could be modified, it's crucial to avoid executing untrusted code that may alter state variables or even [`SELFDESTRUCT`](https://www.evm.codes/#ff) the contract (see [Consensys' smart contracts best practice guide](https://consensys.github.io/smart-contract-best-practices/development-recommendations/general/external-calls/#dont-delegatecall-to-untrusted-code) for more information).*