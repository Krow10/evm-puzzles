# Puzzle 6

### Program

```
[00]	PUSH1	00
[02]	CALLDATALOAD	
[03]	JUMP	
[04]	REVERT	
[05]	REVERT	
[06]	REVERT	
[07]	REVERT	
[08]	REVERT	
[09]	REVERT	
[0a]	JUMPDEST	
[0b]	STOP
```
Hex: `60003556FDFDFDFDFDFD5B00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x000000000000000000000000000000000000000000000000000000000000000a`

## Explanation

[`CALLDATALOAD`](https://www.evm.codes/#35) retrieve the byte in the calldata at the offset specified by the top stack value (offset 0 here from the `PUSH1 00` instruction) as a 32-byte value.

Since the EVM is [big endian](https://en.wikipedia.org/wiki/Endianness), the offset 0 corresponds to the right-most byte in the 32 byte calldata. 

Thus, sending `0x000000000000000000000000000000000000000000000000000000000000000a` as data to the contract will solve this level !