"""
toolbox for testing out simple-salesforce capabilities

@author preston mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports #
# -------------------------------------------------------------------------------------------------------------------- #

import os
import connect_to_salesforce
import queries
import dml_methods
import objects
import pandas as pd


# -------------------------------------------------------------------------------------------------------------------- #
# support methods #
# -------------------------------------------------------------------------------------------------------------------- #

def print_objects(sf):
    """ performs quick query to show all objects in our salesforce instance """
    all_objs = objects.gather_object_names(sf)
    for obj in all_objs:
        print(obj)


def describe_object(obj):
    """ salesforce describe feature returns the following data about an object, reformatting it into readable dict  """
    obj_data = obj.describe()
    action_overrides = obj_data['actionOverrides']
    activateable = obj_data['activateable']
    child_relationships = obj_data['childRelationships']
    compact_layoutable = obj_data['compactLayoutable']
    custom = obj_data['custom']
    customSetting = obj_data['customSetting']
    deletable = obj_data['deletable']
    deprecated_and_hidden = obj_data['deprecatedAndHidden']
    feed_enabled = obj_data['feedEnabled']
    fields = obj_data['fields']
    has_subtypes = obj_data['hasSubtypes']
    key_prefix = obj_data['keyPrefix']
    label = obj_data['label']
    label_plural = obj_data['labelPlural']
    layoutable = obj_data['layoutable']
    listviewable = obj_data['listviewable']
    lookup_layoutable = obj_data['lookupLayoutable']
    mergeable = obj_data['mergeable']
    mruEnabled = obj_data['mruEnabled']
    name = obj_data['name']
    named_layout_infos = obj_data['namedLayoutInfos']
    network_scope_fieldname = obj_data['networkScopeFieldName']
    queryable = obj_data['queryable']
    record_type_infos = obj_data['recordTypeInfos']
    retrieveable = obj_data['retrieveable']
    search_layoutable = obj_data['searchLayoutable']
    searchable = obj_data['searchable']
    supported_scopes = obj_data['supportedScopes']
    triggerable = obj_data['triggerable']
    undeletable = obj_data['undeletable']
    updateable = obj_data['updateable']
    urls = obj_data['urls']

    return {'action overrides': action_overrides, 'activateable': activateable,
            'child_relationships': child_relationships, 'compact_layoutable': compact_layoutable, 'custom': custom,
            'customSetting': customSetting, 'deletable': deletable, 'deprecated_and_hidden': deprecated_and_hidden,
            'feed_enabled': feed_enabled, 'fields': fields, 'has_subtypes': has_subtypes, 'key_prefix': key_prefix,
            'label': label, 'label_plural': label_plural, 'layoutable': layoutable, 'listviewable': listviewable,
            'lookup_layoutable': lookup_layoutable, 'mergeable': mergeable, 'mruEnabled': mruEnabled, 'name': name,
            'named_layout_infos': named_layout_infos, 'network_scope_fieldname': network_scope_fieldname,
            'queryable': queryable, 'record_type_infos': record_type_infos, 'retrieveable': retrieveable,
            'search_layoutable': search_layoutable, 'searchable': searchable, 'supported_scopes': supported_scopes,
            'triggerable': triggerable, 'undeletable': undeletable, 'updateable': updateable, 'urls': urls}


def get_fields(obj_description):
    """ describing the fields off of the object description """
    fields = obj_description['fields']
    fields_dict = {}
    for field in fields:
        aggregatable = field['aggregatable']
        auto_number = field['autoNumber']
        byte_len = field['byteLength']
        calculated = field['calculated']
        calculated_formula = field['calculatedFormula']
        cascade_delete = field['cascadeDelete']
        case_sensative = field['caseSensitive']
        compound_fieldname = field['compoundFieldName']
        controller_name = field['controllerName']
        createable = field['createable']
        custom = field['custom']
        default_value = field['defaultValue']
        default_value_formula = field['defaultValueFormula']
        defaulted_on_create = field['defaultedOnCreate']
        dependent_picklist = field['dependentPicklist']
        deprecated_and_hidden = field['deprecatedAndHidden']
        digits = field['digits']
        display_location_in_dec = field['displayLocationInDecimal']
        encrypted = field['encrypted']
        external_id = field['externalId']
        extra_type_info = field['extraTypeInfo']
        filterable = field['filterable']
        filtered_lookup_info = field['filteredLookupInfo']
        groupable = field['groupable']
        high_scale_num = field['highScaleNumber']
        html_formatted = field['htmlFormatted']
        id_lookup = field['idLookup']
        in_line_help = field['inlineHelpText']
        label = field['label']
        length = field['length']
        mask = field['mask']
        mask_type = field['maskType']
        name = field['name']
        name_field = field['nameField']
        name_pointing = field['namePointing']
        nillable = field['nillable']
        permissionable = field['permissionable']
        picklist_values = field['picklistValues']
        precision = field['precision']
        query_by_dist = field['queryByDistance']
        ref_taget_field = field['referenceTargetField']
        reference_to = field['referenceTo']
        relationship_name = field['relationshipName']
        relationship_order = field['relationshipOrder']
        restricted_delete = field['restrictedDelete']
        restricted_picklist = field['restrictedPicklist']
        scale = field['scale']
        soap_type = field['soapType']
        sortable = field['sortable']
        type = field['type']
        unique = field['unique']
        updateable= field['updateable']
        write_req_master = field['writeRequiresMasterRead']

        fields_dict[name] = {'aggregatable': aggregatable, 'auto_number': auto_number, 'byte_len': byte_len,
                             'calculated': calculated, 'calculated_formula': calculated_formula,
                             'cascade_delete': cascade_delete, 'case_sensative': case_sensative,
                             'compound_fieldname': compound_fieldname, 'controller_name': controller_name,
                             'createable': createable, 'custom': custom, 'default_value': default_value,
                             'default_value_formula': default_value_formula, 'defaulted_on_create': defaulted_on_create,
                             'dependent_picklist': dependent_picklist, 'deprecated_and_hidden': deprecated_and_hidden,
                             'digits': digits, 'display_location_in_dec': display_location_in_dec,
                             'encrypted': encrypted, 'external_id': external_id, 'extra_type_info': extra_type_info,
                             'filterable': filterable, 'filtered_lookup_info': filtered_lookup_info,
                             'groupable': groupable, 'high_scale_num': high_scale_num, 'html_formatted': html_formatted,
                             'id_lookup': id_lookup, 'in_line_help': in_line_help, 'label': label, 'length': length,
                             'mask': mask, 'mask_type': mask_type, 'name': name, 'name_field': name_field,
                             'name_pointing': name_pointing, 'nillable': nillable, 'permissionable': permissionable,
                             'picklist_values': picklist_values, 'precision': precision, 'query_by_dist': query_by_dist,
                             'ref_taget_field': ref_taget_field, 'reference_to': reference_to,
                             'relationship_name': relationship_name, 'relationship_order': relationship_order,
                             'restricted_delete': restricted_delete, 'restricted_picklist': restricted_picklist,
                             'scale': scale, 'soap_type': soap_type, 'sortable': sortable, 'type': type,
                             'unique': unique, 'updateable': updateable, 'write_req_master': write_req_master}

    # for the sake of the toolbox just printing out the field names, storing all in dictionary for reference later
    print("")
    for key in fields_dict.keys():
        print(key)


def select_obj():
    """ selecting and returning a salesforce object from list of objects (using 8 as an example) """
    while True:
        print("\nselect one of the following objects:")
        print("1) Patient")
        print("2) Program")
        print("3) Adverse Event / Product Complaint")
        print("4) Coverage")
        print("5) Caregiver")
        print("6) Document")
        print("7) Task Plan")
        print("8) Specialty Pharmacy")
        selection = input("\n>> ")

        if selection == "1":
            return objects.patient
        elif selection == "2":
            return objects.program
        elif selection == "3":
            return objects.aepc
        elif selection == "4":
            return objects.coverage
        elif selection == "5":
            return objects.caregiver
        elif selection == "6":
            return objects.document
        elif selection == "7":
            return objects.taskplan
        elif selection == "8":
            return objects.sp
        else:
            print("select a valid object")


# -------------------------------------------------------------------------------------------------------------------- #
# main method #
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    # connect to salesforce and instantiate all object names, return them in a list
    sf = connect_to_salesforce.connect()
    all_objects = objects.gather_object_names(sf)

    # create a menu driven help box
    while True:
        print("\nWelcome to the salesforce toolbox, here we will showcase some of the capabilities we have\n")
        print("1) print all objects out")
        print("2) print object fields")
        print("3) quit program")
        selection = input("\n>> ")

        if selection == "1":
            print("")
            print_objects(sf)

        elif selection == "2":
            obj = select_obj()
            obj_description = describe_object(obj)
            get_fields(obj_description)

        elif selection == "3":
            os._exit(0)

        else:
            print("select a valid option please")


# -------------------------------------------------------------------------------------------------------------------- #
# call main #
# -------------------------------------------------------------------------------------------------------------------- #

main()
