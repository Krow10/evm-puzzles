# Puzzle 9

### Program

```
[00]	CALLDATASIZE	
[01]	PUSH1	03
[03]	LT	
[04]	PUSH1	09
[06]	JUMPI	
[07]	REVERT	
[08]	REVERT	
[09]	JUMPDEST	
[0a]	CALLVALUE	
[0b]	CALLDATASIZE	
[0c]	MUL	
[0d]	PUSH1	08
[0f]	EQ	
[10]	PUSH1	14
[12]	JUMPI	
[13]	REVERT	
[14]	JUMPDEST	
[15]	STOP
```
Hex: `36600310600957FDFD5B343602600814601457FD5B00`

### Solution

|Value|<div style="font-weight:normal">2
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x00000000`

## Explanation

The puzzle checks that the data sent is greater than 3 bytes and then multiply this size with the wei amount sent. If the result is equal to 8, the puzzle is solved. 

Basic math will prove that 2\*4 = 8 so to solve this level, one solution can be to send 4 bytes of calldata and 2 wei !