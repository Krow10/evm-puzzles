# Puzzle 8

### Program

```
[00]	CALLVALUE	
[01]	ISZERO	
[02]	NOT	
[03]	PUSH1	07
[05]	JUMPI	
[06]	REVERT	
[07]	JUMPDEST	
[08]	CALLDATASIZE	
[09]	PUSH1	00
[0b]	PUSH1	00
[0d]	CALLDATACOPY	
[0e]	CALLDATASIZE	
[0f]	PUSH1	00
[11]	PUSH1	00
[13]	CREATE	
[14]	SELFBALANCE	
[15]	PUSH1	00
[17]	PUSH1	00
[19]	PUSH1	00
[1b]	PUSH1	00
[1d]	SELFBALANCE	
[1e]	DUP7	
[1f]	GAS	
[20]	CALL	
[21]	PUSH1	01
[23]	EQ	
[24]	PUSH1	28
[26]	JUMPI	
[27]	REVERT	
[28]	JUMPDEST	
[29]	SELFBALANCE	
[2a]	EQ	
[2b]	PUSH1	2f
[2d]	JUMPI	
[2e]	REVERT	
[2f]	JUMPDEST	
[30]	STOP
```
Hex: `341519600757fd5b3660006000373660006000f047600060006000600047865af1600114602857fd5b4714602f57fd5b00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x6001600c60003960016000F330`

## Explanation

I'm not really sure what was the goal with this puzzle. It basically just creates a contract from the `CALLDATA` provided, calls it by sending all its tokens and checks that the balance remains the same after the call (which can't revert).

Again, resetting the hardhat task restore the balance to zero and the puzzle is solved by just deploying a contract that does nothing like the solution provided:
```
[00]	PUSH1	01
[02]	PUSH1	0c
[04]	PUSH1	00
[06]	CODECOPY	
[07]	PUSH1	01
[09]	PUSH1	00
[0b]	RETURN	
[0c]	ADDRESS	
```

Hex:`6001600c60003960016000F330`