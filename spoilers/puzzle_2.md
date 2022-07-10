# Puzzle 2

### Program

```
[00]	CALLVALUE	
[01]	CODESIZE	
[02]	SUB	
[03]	JUMP	
[04]	REVERT	
[05]	REVERT	
[06]	JUMPDEST	
[07]	STOP	
[08]	REVERT	
[09]	REVERT
```
Hex: `34380356FDFD5B00FDFD`

### Solution

|Value|<div style="font-weight:normal">4
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x`

## Explanation

[`CODESIZE`](https://www.evm.codes/#38) returns the total size in bytes of the contract's code (`0xa`, 10 bytes in this case). The [`SUB`](https://www.evm.codes/#03) instruction takes this value and the precedent value from the stack, [`CALLVALUE`](https://www.evm.codes/#34) (that we control) and put the result of the subtraction on the stack for the [`JUMP`](https://www.evm.codes/#56) instruction to use.

Thus sending 4 wei enables to jump to instruction `[06] JUMPDEST`, passing the level !