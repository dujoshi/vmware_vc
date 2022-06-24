################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems, Inc.                                       #
# All Rights Reserved.                                                         #
#                                                                              #
# Name: remove-avevm.py                                                        #
# Purpose: Script to remove a Cisco AVE VM                                     #
#                                                                              #
################################################################################

import argparse
from lib.acivtool.acivtool import AciVTool

if __name__ == "__main__":
    help_example = "Example usage: python remove-avevm.py --vcenter 172.31.100.10 --vc-username 'administrator@vsphere.local'" \
                   " --vc-password 'vcpassword' --host-name 172.31.100.12 --domain-name 'mininet'"
    parser = argparse.ArgumentParser(epilog=help_example)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    parser.add_argument("--vcenter", "--vcHost",  help='vCenter host', required=True)
    parser.add_argument("--vc-username", "--vcUser", type=str, help = 'Enter the login ID', required=True)
    parser.add_argument("--vc-password", "--vcPwd", type =str, help='Enter the password', required=False)
    parser.add_argument("--host-name", "--hostName",  type = str, help = 'Host Name', required=True)
    parser.add_argument("--domain-name", "--domainName", type=str, help = 'Domain/DVS name', required=True)
    help_txt = 'Perform uninstall even if there is/are still active VM(s) using the AVE VM'
    parser.add_argument("--ignore-active-vm", "--ignoreActiveVm", help=help_txt, action='store_true')
    args = parser.parse_args()

    vtool = AciVTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.ave_remove(args.host_name, args.domain_name, False, False, args.ignore_active_vm)

