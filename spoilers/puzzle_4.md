# Puzzle 4

### Program

```
[00]	CALLVALUE	
[01]	CODESIZE	
[02]	XOR	
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
Hex: `34381856FDFDFDFDFDFD5B00`

### Solution

|Value|<div style="font-weight:normal">6
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x`

## Explanation

Similar to [puzzle 2](puzzle_2.md) with a different calculation, this time the [`XOR`](https://www.evm.codes/#18) value of the amount sent and the code size in bytes (`0xc`, 12 bytes in this case) needs to equal the instruction number of `JUMPDEST`, 10.

Calculating `0xc XOR 0xa` gives 6. Thus sending 6 wei to the contract solves this level !