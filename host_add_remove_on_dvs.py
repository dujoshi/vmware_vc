################################################################################
#                                                                              #
# Copyright (c) 2022 Cisco Systems, Inc.                                       #
# All Rights Reserved.                                                         #
#                                                                              #
# Name: content-library.py                                                     #
# Purpose: Script for VMware library content utilities                         #
#                                                                             #
################################################################################

import argparse
import pdb
from lib.vapictool.vapictool import vApicTool

def add(args):
    vtool = vApicTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.add_esx_to_dvs(args.dvs_name, args.esx_host, args.esx_pnic_list)

def remove(args):
    vtool = vApicTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.remove_esx_from_dvs(args.dvs_name, args.esx_host)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vcenter", "--vcHost",  help='vCenter host', required=True)
    parser.add_argument("--vc-username", "--vcUser", type=str, help = 'Enter the login ID', required=True)
    parser.add_argument("--vc-password", "--vcPwd", type =str, help='Enter the password', required=True)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    subparsers = parser.add_subparsers(help='Action')

    create_parser = subparsers.add_parser("Add")
    delete_parser = subparsers.add_parser("Remove")

    mandatory_help_example = "DJ ADD HERE"

    create_parser.add_argument("--dvs_name",  type = str, help = 'Name of the DVS ', required=True)
    create_parser.add_argument("--esx_host", type=str, help='Ip of the esx host to be added to DVS',required=True)
    create_parser.add_argument("--esx_pnic_list", type=str, help="pnic to be linked ',' seperated ex:  'vmnic2,vmnic3' ", required=True)

    create_parser.set_defaults(func=add)
    create_parser.epilog = mandatory_help_example

    mandatory_help_example_delete = "DJ ADD HERE"
    delete_parser.add_argument("--dvs_name",  type = str, help = 'Name of the DVS ', required=True)
    delete_parser.add_argument("--esx_host", type=str, help='Ip of the esx host to be added to DVS',required=True)
    delete_parser.set_defaults(func=remove)
    delete_parser.epilog = mandatory_help_example
    args = parser.parse_args()
    args.func(args)

