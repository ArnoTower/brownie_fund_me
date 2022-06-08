from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    # pass fthe price feed address to our fundme contract

    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    # if not on a development network pull address right from config
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True,
    )

    # yes we would like to publish to etherscan our sourcecode

    # this deploy will make a state change to the blockchain we always need to do from account
    # succesfully verified smart contract to rinkeby

    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
