from brownie import FundMe
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account})

    # this deploy will make a state change to the blockchain we always need to do from account

    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
