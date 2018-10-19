"""
file to store all of the query methods for our salesforce objects

@author preston mackert
"""


# -------------------------------------------------------------------------------------------------------------------- #
# patient methods #
# -------------------------------------------------------------------------------------------------------------------- #

def query(sf, soql):
    query = sf.query_all(soql)
    size = query['totalSize']
    done = query['done']
    records = query['records']

    # return [size, done, records]

    returned_records = []
    for record in records:
        record_fields = {}
        attributes = record['attributes']
        for key in record.keys():
            if record[key] != attributes:
                record_fields[key] = record[key]
        returned_records.append(record_fields)

    return [size, done, returned_records]
