"""
main method for remediation of duplicate patients in PCP

@author preston mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports #
# -------------------------------------------------------------------------------------------------------------------- #

import connect_to_salesforce


# -------------------------------------------------------------------------------------------------------------------- #
# support methods #
# -------------------------------------------------------------------------------------------------------------------- #

def create_new_patient(sf, fn, ln, gender, dob):
    sf.DTPC_Patient__c.create(
        {'First_Name__c': fn, 'Last_Name__c': ln, 'Gender__c': gender, 'Date_of_Birth__c': dob})


def query_all_patients(sf, soql):
    query = sf.query_all(soql)
    size = query['totalSize']
    done = query['done']
    records = query['records']

    return [size, done, records]


# -------------------------------------------------------------------------------------------------------------------- #
# main method #
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    sf = connect_to_salesforce.connect()
    soql = "SELECT First_Name__c, Last_Name__c, Date_of_Birth__c FROM DTPC_Patient__c"
    q_result = query_all_patients(sf, soql)

    print(q_result[0])


# -------------------------------------------------------------------------------------------------------------------- #
# call main #
# -------------------------------------------------------------------------------------------------------------------- #

main()
