"""
make a connection to your salesforce instance using config variables

@author preston mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports #
# -------------------------------------------------------------------------------------------------------------------- #

import config
from simple_salesforce import Salesforce


# -------------------------------------------------------------------------------------------------------------------- #
# connection method #
# -------------------------------------------------------------------------------------------------------------------- #

def connect():
    sf = Salesforce(username=config.username, password=config.password, security_token=config.security_token,
                    domain=config.domain)
    return sf
