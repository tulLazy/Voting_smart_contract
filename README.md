This is a project that already exists in the solidity documentation release 0.8.18

The original smart contract had 2 problems that i solved:
1. Many transactions were needed to assign the rights to vote to all participants.
2. If there was a tie the smart contract wasn't able to forward a tie message

You'll notice that in the original smart contract bytes32 was used to store the name of a proposal,
i used strings because i felt more comfortable usinig strings instead of bytes32
