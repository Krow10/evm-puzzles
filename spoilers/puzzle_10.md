# Puzzle 10

### Program

```
[00]	PUSH1	20
[02]	PUSH1	00
[04]	PUSH1	00
[06]	CALLDATACOPY	
[07]	PUSH1	00
[09]	MLOAD	
[0a]	PUSH32	f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
[2b]	AND	
[2c]	PUSH1	20
[2e]	PUSH1	20
[30]	PUSH1	00
[32]	CALLDATACOPY	
[33]	PUSH1	00
[35]	MLOAD	
[36]	OR	
[37]	PUSH32	abababababababababababababababababababababababababababababababab
[58]	EQ	
[59]	PUSH1	5d
[5b]	JUMPI	
[5c]	REVERT	
[5d]	JUMPDEST	
[5e]	STOP
```
Hex: `602060006000376000517ff0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f01660206020600037600051177fabababababababababababababababababababababababababababababababab14605d57fd5b00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0xa0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a00b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b`

## Explanation

The last challenge !

Going step by step, the equation that needs to be solved for this level is the following:
```
(CALLDATA[0:32] && 0xf0...f0) || CALLDATA[32:64] = 0xab...ab
```

Hence the solution:
```
   0xa0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0 / CALLDATA[0:32]
&& 0xf0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
---------------------------------------------------------------------
   0xa0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0
|| 0x0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b / CALLDATA[32:64]
---------------------------------------------------------------------
   0xabababababababababababababababababababababababababababababababab
```