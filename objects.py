"""
setting all of the PCP objects to their names so that they are easier to use

@author preston mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports #
# -------------------------------------------------------------------------------------------------------------------- #

import connect_to_salesforce
import queries

# -------------------------------------------------------------------------------------------------------------------- #
# setting all objects #
# -------------------------------------------------------------------------------------------------------------------- #

sf = connect_to_salesforce.connect()
patient = sf.DTPC_Patient__c
aepc = sf.DTPC_Adverse_Event__c
caregiver = sf.DTPC_Caregiver__c
coverage = sf.DTPC_Coverage__c
document = sf.DTPC_Document__c
program = sf.DTPC_Program__c
sp = sf.DTPC_Specialty_Pharmacy__c
taskplan = sf.DTPC_Task_Plan__c
cap = sf.DTPC_Consent_Auth_Preference__c


# -------------------------------------------------------------------------------------------------------------------- #
# methods #
# -------------------------------------------------------------------------------------------------------------------- #

def gather_object_names(sf):
    """ returns a list of all object names in string format """
    # use SOQL statement to get all API names of objects
    soql = "SELECT QualifiedApiName FROM EntityDefinition order by QualifiedApiName"
    query_objects = queries.query(sf, soql)

    # formatting objects into a list (stored in a dict with same key)
    return_objects = []
    for the_object in query_objects:
        return_objects.append(the_object['QualifiedApiName'])
        
    return return_objects
