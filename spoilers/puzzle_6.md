# Puzzle 6

### Program

```
[00]	PUSH32	fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0
[21]	CALLVALUE	
[22]	ADD	
[23]	PUSH1	01
[25]	EQ	
[26]	PUSH1	2a
[28]	JUMPI	
[29]	REVERT	
[2a]	JUMPDEST	
[2b]	STOP
```
Hex: `7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03401600114602a57fd5b00`

### Solution

|Value|<div style="font-weight:normal">17
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x`

## Explanation

This puzzle showcases an important problem developers needs to be aware of when manipulating fixed size data in memory: it can [overflow](https://en.wikipedia.org/wiki/Integer_overflow) – or even [underflow](https://en.wikipedia.org/wiki/Arithmetic_underflow) sometimes !

Since [Solidity v0.8.0](https://docs.soliditylang.org/en/latest/080-breaking-changes.html), arithmetic operations that triggers an overflow or underflow gets reverted by default. But this behavior happens thanks to the compiler which surrounds arithmetic operations with additional checks. Something that doesn't apply here when working with bytecode directly.

Hence, the value pushed on the stack by `[00]` is 15 short of the maximum value a 32-byte variable can hold (2\*\*256 - 1). By providing a `CALLVALUE` of 17, the `ADD` operation will make the value rollback to 1, validating the puzzle !