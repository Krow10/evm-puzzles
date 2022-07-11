# evm-puzzles

Getting more familiar with low-level EVM development and technicalities.

## Why ?

When focusing on the security aspect about a particular technology, it's important to be familiar with it on every level. Even more when we're talking about a complex system like the [Ethereum Virtual Machine (EVM)](https://www.evm.codes/about) or smart contract development in general where security-related bugs can occur at every step, from the original source code getting compiled to the EVM executing the assembly instructions.

I've learned to be familiar with assembly on x86 and x64 architectures prior, mostly via disassembly of Windows binaries for the purpose of finding exploits or bypassing certain restrictions. I hope to achieve the same level of understanding with EVM bytecode to be able to figure out some of its subtelties (and their potential abuse !).

Starting with theses puzzle should enable me to get going on this path.

## What ?

Write-up of my solutions to the puzzles can be found in the [spoilers](/spoilers/) directory with corresponding markdown files for each puzzle.

## Next ?

See more EVM puzzle solving on the [more-evm-puzzles](https://github.com/Krow10/evm-puzzles/tree/more-evm-puzzles) branch !

# Forked original README.md

A collection of EVM puzzles. Each puzzle consists on sending a successful transaction to a contract. The bytecode of the contract is provided, and you need to fill the transaction data that won't revert the execution.

## How to play

Clone this repository and install its dependencies (`npm install` or `yarn`). Then run:

```
npx hardhat play
```

And the game will start.

In some puzzles you only need to provide the value that will be sent to the contract, in others the calldata, and in others both values.

You can use [`evm.codes`](https://www.evm.codes/)'s reference and playground to work through this.
