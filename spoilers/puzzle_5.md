# Puzzle 5

### Program

```
[00]	CALLVALUE	
[01]	DUP1	
[02]	MUL	
[03]	PUSH2	0100
[06]	EQ	
[07]	PUSH1	0C
[09]	JUMPI	
[0a]	REVERT	
[0b]	REVERT	
[0c]	JUMPDEST	
[0d]	STOP	
[0e]	REVERT	
[0f]	REVERT
```
Hex: `34800261010014600C57FDFD5B00FDFD`

### Solution

|Value|<div style="font-weight:normal">16
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x`

## Explanation

The [`DUP1`](https://www.evm.codes/#80) opcode duplicates the first value of the stack, giving the two required arguments for the [`MUL`](https://www.evm.codes/#02) instruction to be multiplied. [`PUSH2`](https://www.evm.codes/#18) then places a 2 byte value (one byte only goes up to `0xFF` or 255) equal to 256 which is then compared to the result of the `MUL` operation.

If both values are equal, `1` is pushed on the stack and the address of the `JUMPDEST` instruction is also subsequently pushed on the stack. [`JUMPI`](https://www.evm.codes/#18) will then jump, only if `EQ` returned a non-zero value.

Since 16\*16 = 256, sending 16 wei to the contract will solve this level !