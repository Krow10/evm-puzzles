# more-evm-puzzles

Getting more familiar with low-level EVM development and technicalities.

## Why ?

Part 2 of understanding EVM bytecode through puzzles !

See [README.md](evm-puzzles/blob/master/README.md) on master branch for the original purpose in doing theses challenges.

## What ?

Write-up of my solutions to the puzzles can be found in the [spoilers](/spoilers/) directory with corresponding markdown files for each puzzle.

# Forked original README.md

Here are 10 more puzzles, inspired by the 10 EVM puzzles created by [@fvictorio](https://github.com/fvictorio/evm-puzzles). These ones are harder and more focused on the CREATE and CALL opcodes. Have fun!

Each puzzle consists of sending a successful transaction to a contract. The bytecode of the contract is provided, and you need to fill the transaction CALLDATA and CALLVALUE that won't revert the execution.

## How to play

Clone this repository and install its dependencies (`npm install` or `yarn`). Then run:

```
npx hardhat play
```

And the game will start.

In some puzzles you only need to provide the value that will be sent to the contract, in others the calldata, and in others both values.

You can use [`evm.codes`](https://www.evm.codes/)'s reference and playground to work through this.