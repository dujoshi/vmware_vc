################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems, Inc.                                       #
# All Rights Reserved.                                                         #
#                                                                              #
# Name: remove-vpodvm.py                                                       #
# Purpose: Script to remove all the vPod VMS of a vPod                         #
#                                                                              #
################################################################################

import argparse
from lib.acivtool.acivtool import AciVTool

if __name__ == "__main__":
    help_example = "Example usage: python remove-avevm.py --vcenter 172.31.100.10 --vc-username 'administrator@vsphere.local'" \
                   " --vc-password 'vcpassword' --vpod-id 2"
    parser = argparse.ArgumentParser(epilog=help_example)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    parser.add_argument("--vcenter", "--vcHost",  help='vCenter host', required=True)
    parser.add_argument("--vc-username", "--vcUser", type=str, help = 'Enter the login ID', required=True)
    parser.add_argument("--vc-password", "--vcPwd", type =str, help='Enter the password', required=False)
    parser.add_argument("--vpod-id", type=str, help='vPOD ID', required=True)

    args = parser.parse_args()

    vtool = AciVTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.vpod_remove(None, None, args.vpod_id)