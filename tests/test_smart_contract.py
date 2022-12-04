from scripts.helpful_scripts import get_account
from brownie import Voting


def test_giveRights_delegate_vote_getWinner():
    chairperson = get_account()
    account_1 = get_account(1)
    account_2 = get_account(2)
    account_3 = get_account(3)
    proposals = [
        "Young Thug",
        "Lil baby",
        "Gunna",
        "Future",
        "Migos",
        "Drake",
        "Travis scott",
        "Lil Uzi Vert",
        "21 Savage",
        "Eminem",
        "Meek Mill",
        "Nav",
        "Ye",
        "Kodak Black",
    ]
    addresses_that_can_vote = [account_1, account_2, account_3]
    voting_contract = Voting.deploy(proposals, {"from": chairperson})

    # Giving right to vote.
    give_right_tx = voting_contract.giveRightToVote(
        addresses_that_can_vote, {"from": chairperson}
    )
    give_right_tx.wait(1)

    # Asserting if the accounts have right to vote.
    for i in range(len(addresses_that_can_vote)):
        assert voting_contract.voters(addresses_that_can_vote[i])[0] == 1

    # Chairperson delegating his vote to account_2.
    delegate = voting_contract.delegate(account_2, {"from": chairperson})
    delegate.wait(1)

    # Account_1 delegating his vote to chairperson.
    delegate_1 = voting_contract.delegate(chairperson, {"from": account_1})
    delegate_1.wait(1)

    # Asserting account_2 has 3 "weights". 1 --> his/her(or whatever you want to identify as), 2 --> chairperson, 3--> account_1
    assert voting_contract.voters(account_2)[0] == 3

    # Account_3 giving his vote to "Migos". Rest in peace Takeoff
    vote = voting_contract.vote(4, {"from": account_3})
    vote.wait(1)

    # Account_2 giving his votes to "Young Thug"
    vote_1 = voting_contract.vote(0, {"from": account_2})
    vote_1.wait(1)

    # Asserting Migos got one vote
    assert voting_contract.proposals(4)[1] == 1

    # Asserting Young Thug got 3 votes
    assert voting_contract.proposals(0)[1] == 3

    # Asserting Young Thug the  is the winner
    assert voting_contract.checkIfTieOrNot() == "Young Thug"

    # #FreeYoungThug
    # #FreeGunna
    # #FreeYSL
