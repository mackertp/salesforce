"""
file to store all of the DML methods available for our salesforce objects

@author preston mackert
"""


# -------------------------------------------------------------------------------------------------------------------- #
# creation methods #
# -------------------------------------------------------------------------------------------------------------------- #

def create_new_patient(sf, fn, ln, gender, dob):
    sf.DTPC_Patient__c.create({'First_Name__c': fn, 'Last_Name__c': ln, 'Gender__c': gender, 'Date_of_Birth__c': dob})
