# Puzzle 5

### Program

```
[00]	PUSH1	20
[02]	CALLDATASIZE	
[03]	GT	
[04]	PUSH1	08
[06]	JUMPI	
[07]	REVERT	
[08]	JUMPDEST	
[09]	CALLDATASIZE	
[0a]	PUSH1	00
[0c]	PUSH1	00
[0e]	CALLDATACOPY	
[0f]	CALLDATASIZE	
[10]	MSIZE	
[11]	SUB	
[12]	PUSH1	03
[14]	EQ	
[15]	PUSH1	19
[17]	JUMPI	
[18]	REVERT	
[19]	JUMPDEST	
[1a]	STOP
```
Hex: `60203611600857FD5B366000600037365903600314601957FD5B00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`

## Explanation

The first check to pass is that the `CALLDATASIZE` must be greater than `0x20` (32 bytes).

Next, the `CALLDATACOPY` operation writes this data to memory, triggering a memory expansion since the memory layout of the EVM is made of 32-bytes slots.

Hence, the resulting call to [`MSIZE`](https://www.evm.codes/#59), which tracks "the highest offset that was accessed in the current execution", returns `0x40` as the first condition required that the `CALLDATASIZE` cannot fit in one memory slot.

Knowing this, we can determine the last condition to solve the puzzle as `0x40 - CALLDATASIZE = 3` which gives a size of 61 bytes for the calldata. 