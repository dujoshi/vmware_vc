################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems, Inc.                                       #
# All Rights Reserved.                                                         #
#                                                                              #
# Name: content-library.py                                                     #
# Purpose: Script for VMware library content utilities                         #
#                                                                              #
################################################################################

import argparse
import pdb
from lib.acivtool.acivtool import AciVTool

def create(args):
    print('\n inside create def')
    vtool = AciVTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.cl_create_dvs(args.name, args.datacenter, args.version)


def upload(args):
    print('\n inside delete def')
    pdb.set_trace()


def delete(args):
    print('\n inside delete def')
    pdb.set_trace()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vcenter", "--vcHost",  help='vCenter host', required=True)
    parser.add_argument("--vc-username", "--vcUser", type=str, help = 'Enter the login ID', required=True)
    parser.add_argument("--vc-password", "--vcPwd", type =str, help='Enter the password', required=False)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    subparsers = parser.add_subparsers(help='Action')

    create_parser = subparsers.add_parser("Create")
    upload_parser = subparsers.add_parser("Upload")
    delete_parser = subparsers.add_parser("Remove")

    mandatory_help_example = "Example usage: python content-library.py --vcHost 172.31.100.10 --vcUser 'administrator@vsphere.local'" \
                             "  --vcPwd 'vcpassword' "

    create_parser.add_argument("--name",  type = str, help = 'Name of the new Content Library to create', required=True)
    create_parser.add_argument("--datacenter", type=str, help='Name of Datacenter the Datastore belongs to',required=True)
    create_parser.add_argument("--version", type=str, help='Name of Datastore to use to back the Content Library', required=True)
    create_parser.add_argument("--infra_vlan", type=str, help='Name of Datastore to use to back the Content Library',
                               required=True)

    create_parser.set_defaults(func=create)
    create_parser.epilog = mandatory_help_example + "Create --name ave-content-lib --datacenter dc1 --datastore datastore01"


    upload_parser.add_argument("--library",  type = str, help = 'Name of Content Library', required=True)
    upload_parser.add_argument("--item", type=str, help='Name of the new item to create', required=True)
    upload_parser.add_argument("--path", type=str, help='Path to the .ovf file', required=True)
    upload_parser.add_argument("--vmdk-ds-path", type=str, help='Path to the vmdk file on a datastore volume', required=False)
    upload_parser.set_defaults(func=upload)
    upload_parser.epilog = mandatory_help_example + "Upload --library ave-content-lib --item cisco-ave-1 --path /home/user/cisco-ave.ovf"

    delete_parser.add_argument("--library",  type = str, help = 'Name of Content Library', required=True)
    delete_parser.add_argument("--item", type=str, help='Name of the item to delete', required=True)
    delete_parser.set_defaults(func=delete)
    delete_parser.epilog = mandatory_help_example + "Remove --library ave-content-lib --item cisco-ave-1"
    import pdb
    pdb.set_trace()
    args = parser.parse_args()
    args.func(args)

