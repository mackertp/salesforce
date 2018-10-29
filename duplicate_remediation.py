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
from fuzzywuzzy import fuzz
import re


# -------------------------------------------------------------------------------------------------------------------- #
# support methods #
# -------------------------------------------------------------------------------------------------------------------- #

def verify_duplicate_patients(sf, p1, p2):
    """ this method follows the logic in the SOP for verifying duplicate patients in the PCP """
    soql = "SELECT First_Name__c, Last_Name__c, Date_of_Birth__c, Gender__c, Patient_Email__c, Primary_State__c, " \
           "Primary_City__c, Primary_Street__c, Primary_ZIP__c, Phone_1_Details__c FROM DTPC_Patient__c " \
           "WHERE Patient_Unique_Id__c='%s'" % p1

    patient_1 = queries.query(sf, soql)

    soql = "SELECT First_Name__c, Last_Name__c, Date_of_Birth__c, Gender__c, Patient_Email__c, Primary_State__c, " \
           "Primary_City__c, Primary_Street__c, Primary_ZIP__c, Phone_1_Details__c  FROM DTPC_Patient__c " \
           "WHERE Patient_Unique_Id__c='%s'" % p2

    patient_2 = queries.query(sf, soql)

    print(patient_1)
    print(patient_2)

    # because we are using unique ID, we know there is only one record in the return string
    p1 = patient_1[0]

    p1_fname = p1['First_Name__c']
    p1_lname = p1['Last_Name__c']
    p1_name = p1_fname + p1_lname
    p1_name = re.sub('DUPLICATE', '', p1_name)

    p1_dob = p1['Date_of_Birth__c']
    p1_gender = p1['Gender__c']
    p1_email = p1['Patient_Email__c']
    p1_addr = p1['Primary_Street__c'] + ', ' + p1['Primary_City__c'] + ', ' + p1['Primary_ZIP__c']

    p2 = patient_2[0]
    p2_fname = p2['First_Name__c']
    p2_lname = p2['Last_Name__c']
    p2_name = p2_fname + p2_lname
    p2_name = re.sub('DUPLICATE', '', p2_name)

    p2_dob = p2['Date_of_Birth__c']
    p2_gender = p2['Gender__c']
    p2_email = p2['Patient_Email__c']
    p2_addr = p2['Primary_Street__c'] + ', ' + p1['Primary_City__c'] + ', ' + p1['Primary_ZIP__c']

    if p1_name == p2_name and p1_dob == p2_dob:
        return True

    elif p1_name == p2_name and p1_gender == p2_gender:
        return True

    elif p1_email == p2_email and p1_email is not None:
        return True

    elif fuzz.ratio(p1_name, p2_name) > 85 and fuzz.ratio(p1_addr, p2_addr) > 85:
        return True

    else:
        while True:
            print("These patients need manual verification, type T to verify, F to invalidate")
            print(p1)
            print(p2)
            select = input("\n>> ")

            if select == 'T':
                return True
            elif select == 'F':
                return False


def verify_person_participants(sf, p1, p2):
    """ this method follows the logic in the SOP for verifying duplicate person participants """
    soql = "Need to find out how to access patient participants since they are not objects"


def remediate_patients(sf, p1, p2):
    """ method to perform data remediation on two duplicate patients """
    soql = "SELECT Id, DTPC_Patient_Formal_Name__c, Patient_Status__c FROM DTPC_Patient__c WHERE Patient_Unique_Id__c='%s'" % p1
    patient_1 = queries.query(sf, soql)

    soql = "SELECT DTPC_Patient_Formal_Name__c, Patient_Status__c FROM DTPC_Patient__c WHERE Patient_Unique_Id__c='%s'" % p2
    patient_2 = queries.query(sf, soql)

    patient_1_id = patient_1[0]['Id']
    soql = "SELECT Patient__c FROM DTPC_Program__c WHERE Patient__c='%s'" % patient_1_id
    p1_programs = queries.query(sf, soql)

    #print(patient_1)
    #print(patient_2)

    #print(p1_programs)


# -------------------------------------------------------------------------------------------------------------------- #
# main method #
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    # connect to salesforce
    sf = connect_to_salesforce.connect()

    # testing out the different query methods
    patient_1_id = "1005130"
    patient_2_id = "1005118"
    patient_verification = verify_duplicate_patients(sf, patient_1_id, patient_2_id)
    if patient_verification:
        remediate_patients(sf, patient_1_id, patient_2_id)



# -------------------------------------------------------------------------------------------------------------------- #
# call main #
# -------------------------------------------------------------------------------------------------------------------- #

main()
