import connect_to_salesforce
import dml_methods
import queries
import objects
from xlrd import open_workbook
import openpyxl


def read_report(report_name):
    # read the email consent remediation report
    book = open_workbook(report_name)
    sheet = book.sheet_by_index(0)

    # read header values
    keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]

    dict_list = []
    for row_index in range(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in range(sheet.ncols)}
        dict_list.append(d)

    return dict_list


def main():
    sf = connect_to_salesforce.connect()
    cap_programs = read_report('capremediation.xlsx')
    ids = []
    for program in cap_programs:
        ids.append(program['Program: ID'])

    statuses = []
    for id in ids:
        soql = "SELECT DTPC_Status__c FROM DTPC_Program__c WHERE Id='%s'" % id
        response = queries.query(sf, soql)
        for status in response:
            statuses.append(status['DTPC_Status__c'])

    print(set(statuses))


main()
