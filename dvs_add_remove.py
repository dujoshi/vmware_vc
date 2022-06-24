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

def create(args):
    vtool = vApicTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.dvs_create(args.name, args.datacenter, args.version)
    vtool.dvs_create_pg(args.name, args.infra_vlan)

def upload(args):
    pdb.set_trace()

def delete(args):
    vtool = vApicTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.dvs_delete(args.name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vcenter", "--vcHost",  help='vCenter host', required=True)
    parser.add_argument("--vc-username", "--vcUser", type=str, help = 'Enter the login ID', required=True)
    parser.add_argument("--vc-password", "--vcPwd", type =str, help='Enter the password', required=True)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    subparsers = parser.add_subparsers(help='Action')

    create_parser = subparsers.add_parser("Create")
    delete_parser = subparsers.add_parser("Remove")

    mandatory_help_example = "dvs_add_remove.py --vcHost 'x.x.x.x' --vcUser 'administrator@vsphere.local' --vcPwd '*****' Create --name vAPIC" \
                             " --datacenter MSITE-DC --version 6.5 --infra_vlan 4000"

    create_parser.add_argument("--name",  type = str, help = 'Name of the new DVS to be created', required=True)
    create_parser.add_argument("--datacenter", type=str, help='Name of Datacenter where DVS will be created',required=True)
    create_parser.add_argument("--version", type=str, help='Verision of DVS to be created', required=True)
    create_parser.add_argument("--infra_vlan", type=str, help='infra_vlan number to be assigned to Infra Vlan PG',
                               required=True)
    create_parser.set_defaults(func=create)
    create_parser.epilog = mandatory_help_example

    mandatory_help_example_delete = "python dvs_add_remove.py --vcHost 10.197.145.50 --vcUser administrator@vsphere.local --vcPwd Insieme\!123 Remove --name vAPIC"


    delete_parser.add_argument("--name", type=str, help='Name of the dvs to be deleted', required=True)
    delete_parser.set_defaults(func=delete)
    delete_parser.epilog = mandatory_help_example + "Remove --name"
    args = parser.parse_args()
    args.func(args)

