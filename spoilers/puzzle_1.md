# Puzzle 1

### Program

```
[00]	CALLDATASIZE	
[01]	CALLVALUE	
[02]	EXP	
[03]	JUMP	
[04]	INVALID	
[05]	INVALID	
     ...
[3e]	INVALID	
[3f]	INVALID	
[40]	JUMPDEST	
[41]	PC	
[42]	CALLDATASIZE	
[43]	ADD	
[44]	JUMP	
[45]	INVALID	
[46]	INVALID	
[47]	JUMPDEST	
[48]	STOP
```
Hex: `36340A56FEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFEFE5B58360156FEFE5B00`

### Solution

|Value|<div style="font-weight:normal">2
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x000000000000`

## Explanation

[`EXP`](https://www.evm.codes/#0a) will return the result of `CALLVALUE ^ CALLDATASIZE`. To reach the end of the program, this value needs to equal `0x40` reaching the first `JUMPDEST`.

Out of the 3 possibles solutions (2^6, 4^3 and 8^2), only one will work for the next `JUMP` to go to instruction `0x47` as `PC` will return `0x41` and add that to `CALLDATASIZE` (requiring it to be equal to 6).

Hence, sending 2 wei and a calldata of 6 bytes will solve this puzzle !