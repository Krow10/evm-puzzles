# Puzzle 9

### Program

```
[00]	CALLVALUE	
[01]	PUSH1	00
[03]	MSTORE	
[04]	PUSH1	20
[06]	PUSH1	00
[08]	SHA3	
[09]	PUSH1	F8
[0b]	SHR	
[0c]	PUSH1	A8
[0e]	EQ	
[0f]	PUSH1	16
[11]	JUMPI	
[12]	REVERT	
[13]	REVERT	
[14]	REVERT	
[15]	REVERT	
[16]	JUMPDEST	
[17]	STOP
```
Hex: `34600052602060002060F81C60A814601657FDFDFDFD5B00`

### Solution

|Value|<div style="font-weight:normal">47
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x`

## Explanation

This puzzle requires a bit of guess work taken to the next level: find a value whose `Keccak256()` hash start with the byte `0xa8`.

Enumerating values by hand would be tedious, hence, I putted together a little [python script](puzzle_9.py) for searching the first value that satisfies the puzzle.

Turns out the hash of value 47 is `a813484aef6fb598f9f753daf162068ff39ccea4075cb95e1a30f86995b5b7ee`, solving the puzzle ! 