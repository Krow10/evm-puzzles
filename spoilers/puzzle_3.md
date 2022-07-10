# Puzzle 3

### Program

```
[00]	CALLDATASIZE	
[01]	JUMP	
[02]	REVERT	
[03]	REVERT	
[04]	JUMPDEST	
[05]	STOP
```
Hex: `3656FDFD5B00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x00000000`

## Explanation

[`CALLDATASIZE`](https://www.evm.codes/#36) returns the total size in bytes of the data sent to the contract.

Thus sending 4, 1-byte instructions enables to jump to instruction `[04] JUMPDEST`, passing the level !