################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems, Inc.                                       #
# All Rights Reserved.                                                         #
#                                                                              #
# Name: get-vpodvm.py                                                          #
# Purpose: Script to get Cisco vPod VM information                             #
#                                                                              #
################################################################################

import argparse
from lib.acivtool.acivtool import AciVTool


if __name__ == "__main__":
    help_example = "Example usage: python get-vpodvm.py --vcenter 172.31.100.10 --vc-username 'administrator@vsphere.local'" \
                   " --vc-password 'vmware123'"
    parser = argparse.ArgumentParser(epilog=help_example)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    parser.add_argument("--vcenter",  help='vCenter IP / FQDN', required=True)
    parser.add_argument("--vc-username", type=str, help = 'vCenter username', required=True)
    parser.add_argument( "--vc-password", type =str, help='vCenter user password' , required=False)
    args = parser.parse_args()

    vtool = AciVTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.vpod_get(output='print')

