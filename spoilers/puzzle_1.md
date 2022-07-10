# Puzzle 1

### Program

```
[00]	CALLVALUE	
[01]	JUMP	
[02]	REVERT	
[03]	REVERT	
[04]	REVERT	
[05]	REVERT	
[06]	REVERT	
[07]	REVERT	
[08]	JUMPDEST	
[09]	STOP
```
Hex: `3456FDFDFDFDFDFD5B00`

### Solution

|Value|<div style="font-weight:normal">8
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x`

## Explanation

Using the documentation over at [EVM Codes](https://www.evm.codes/), we can figure out the [`CALLVALUE`](https://www.evm.codes/#34) opcode puts the value sent to the top of the stack.
[`JUMP`](https://www.evm.codes/#56) takes the stack value and checks for a [`JUMPDEST`](https://www.evm.codes/#5b) instruction at the offset specified.

Thus sending 8 wei enables to jump to the end of the program, passing the level !