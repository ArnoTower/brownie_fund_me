
#we added the get_account into its own file (this)
# we are saying if network is in development use account 0 syntex otherwise pull from my config
from brownie import network, config, accounts

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])