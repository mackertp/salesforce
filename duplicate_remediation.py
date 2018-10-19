"""
main method for remediation of duplicate patients in PCP platform

@author preston mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports #
# -------------------------------------------------------------------------------------------------------------------- #

import connect_to_salesforce
import queries
import dml_methods
import pandas as pd


def verify_duplicate_patients(p1, p2):
    print("verifying duplicates...")


# -------------------------------------------------------------------------------------------------------------------- #
# main method #
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    # connect to salesforce
    sf = connect_to_salesforce.connect()

    # testing out the different query methods

    for item in sf.DTPC_Patient__c.describe():
        print(item)

    """
    p1_soql = "SELECT Unique_Patient_Id__c FROM DTPC_Patient__c"
    p2_soql = "SELECT F"
    p1 = queries.query_patients(sf, p1_soql)
    p2 = queries.query_patients(sf, p2_soql)
    # print(p1)
    # print(p2)
    """

# -------------------------------------------------------------------------------------------------------------------- #
# call main #
# -------------------------------------------------------------------------------------------------------------------- #

main()
