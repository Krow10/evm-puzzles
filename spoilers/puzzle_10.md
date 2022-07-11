# Puzzle 10

### Program

```
[00]	CODESIZE	
[01]	CALLVALUE	
[02]	SWAP1	
[03]	GT	
[04]	PUSH1	08
[06]	JUMPI	
[07]	REVERT	
[08]	JUMPDEST	
[09]	CALLDATASIZE	
[0a]	PUSH2	0003
[0d]	SWAP1	
[0e]	MOD	
[0f]	ISZERO	
[10]	CALLVALUE	
[11]	PUSH1	0A
[13]	ADD	
[14]	JUMPI	
[15]	REVERT	
[16]	REVERT	
[17]	REVERT	
[18]	REVERT	
[19]	JUMPDEST	
[1a]	STOP
```
Hex: `38349011600857FD5B3661000390061534600A0157FDFDFDFD5B00`

### Solution

|Value|<div style="font-weight:normal">15
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x000000`

## Explanation

Following the flow of instructions, the last `[14] JUMPI` instruction will succeed if the following equation is valid : 

```
CALLVALUE + 0xa = 0x19 = 25
^^^^^^^^^   ^^^   ^^^^
  [10]      [11]  [14]
``` 

with `CALLVALUE < CODESIZE = 0x1b = 27`.

Also, the `IS_ZERO` instruction requires the `CALLDATASIZE` to be a multiple of 3 as per the `MOD` instruction used to conditionnaly make the jump at `[14]`.

Hence, the solution is to set `CALLDATASIZE` to 3 (making the modulus equal 0, `IS_ZERO` returning 1), and `CALLVALUE` to 15 = 25 - 10.

*Note: The author rightfully crafted the last jump offset to be greater than the previous `[08] JUMPDEST` otherwise it would have been possible to make an infinite loop !*