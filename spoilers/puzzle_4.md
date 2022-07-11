# Puzzle 4

### Program

```
[00]	ADDRESS	
[01]	BALANCE	
[02]	CALLDATASIZE	
[03]	PUSH1	00
[05]	PUSH1	00
[07]	CALLDATACOPY	
[08]	CALLDATASIZE	
[09]	PUSH1	00
[0b]	ADDRESS	
[0c]	BALANCE	
[0d]	CREATE	
[0e]	BALANCE	
[0f]	SWAP1	
[10]	DIV	
[11]	PUSH1	02
[13]	EQ	
[14]	PUSH1	18
[16]	JUMPI	
[17]	REVERT	
[18]	JUMPDEST	
[19]	STOP
```
Hex: `30313660006000373660003031F0319004600214601857FD5B00`

### Solution

|Value|<div style="font-weight:normal">2
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x60008080806001815AF1600080F3`

## Explanation

Here's a breakdown of the puzzle code :
1. It gets it's balance (with two instructions although [`SELFBALANCE`]() does it in one, gas savings !)
2. It creates a contract with the calldata and sends all of its ether to it.
3. Then it expects the created contract's balance to be half of its original balance to validate the puzzle.

Knowing this, we can deploy a dummy contract (since it will never be called) and use the init code to burn or send back half of the ether received.

This is what the calldata does :
```
[00]	PUSH1	00 # retSize (unused)
[02]	DUP1	   # retOffset (unused)
[03]	DUP1	   # argsSize (unused)
[04]	DUP1	   # argsOffset (unused)
[05]	PUSH1	01 # value in wei to burn
[07]	DUP2	   # address set to burn address (0x00...00)
[08]	GAS	       # gas for the call
[09]	CALL	   # send the value
[0a]	PUSH1	00 
[0c]	DUP1	
[0d]	RETURN     # dummy contract return from CREATE
```

By sending 2 wei along with the calldata, the created contract will send 1 wei to the burn address, solving the puzzle !

*Note: when trying this I had trouble with both the simulator and the hardhat challenge since the balance is preserved between attempts. To validate, simply reload the hardhat task.*