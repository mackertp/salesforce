"""
creating variables for login credentials

in order to receive the API security token, copy and paste the following URL into the search box using the proper
salesforce instance:

https://[SalesforceDomainHere]/_ui/system/security/ResetApiTokenEdit?retURL=%2Fui%2Fsetup%2FSetup%3Fsetupid%3DPersonalInfo&setupid=ResetApiToken

@author preston mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# config variables #
# -------------------------------------------------------------------------------------------------------------------- #

username = "salesforce username"
password = "salesforce password"
security_token = "salesforce API security token"
domain = 'use test if development sandbox, do not include a domain if production'
