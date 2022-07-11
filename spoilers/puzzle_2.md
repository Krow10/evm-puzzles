# Puzzle 2

### Program

```
[00]	CALLDATASIZE	
[01]	PUSH1	00
[03]	PUSH1	00
[05]	CALLDATACOPY	
[06]	CALLDATASIZE	
[07]	PUSH1	00
[09]	PUSH1	00
[0b]	CREATE	
[0c]	PUSH1	00
[0e]	DUP1	
[0f]	DUP1	
[10]	DUP1	
[11]	DUP1	
[12]	SWAP5	
[13]	GAS	
[14]	CALL	
[15]	RETURNDATASIZE	
[16]	PUSH1	0a
[18]	EQ	
[19]	PUSH1	1F
[1b]	JUMPI	
[1c]	INVALID	
[1d]	INVALID	
[1e]	INVALID	
[1f]	JUMPDEST	
[20]	STOP
```
Hex: `3660006000373660006000F0600080808080945AF13D600a14601F57FEFEFE5B00`

### Solution

|Value|<div style="font-weight:normal">0
|-|-
|<div style="font-weight:bold">Data|<div style="font-weight:normal">`0x6005600c60003960056000F3600a6000f3`

## Explanation

Looking through the code, it looks similar to [puzzle 8](../../blob/master/spoilers/puzzle_8.md) of the original puzzles !

It requires to initialize a contract (`[00]` to `[0b]`) that will be called (`[0c]` to `[14]`) and expect the return size of the call to be equal to `0xa` (10 bytes) to make the `JUMP`.

The solution provided here translate to this code :
```
[00]	PUSH1	05  # Size of deployed contract code
[02]	PUSH1	0c  # Offset from which the deployed contract starts in this context 
[04]	PUSH1	00	# Memory location to store deployed contract
[06]	CODECOPY    # Copy the contract code to memory
[07]	PUSH1	05  # Size of deployed contract code
[09]	PUSH1	00  # Memory location of deployed contract
[0b]	RETURN	    # Return to calling context (return from CREATE)
[0c]	PUSH1	0a  # Size of data to return
[0e]	PUSH1	00  # Memory location of data (could be anything under 22)
[10]	RETURN		# Return from call
```

The `RETURNDATASIZE` instruction will return 10 and the puzzle will be solved !