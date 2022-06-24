################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems, Inc.                                       #
# All Rights Reserved.                                                         #
#                                                                              #
# Name: new-vpodvm.py                                                           #
# Purpose: Script to deploy a new pair of Cisco vSpine/vLeaf VM                #
#                                                                              #
################################################################################

import argparse
from lib.acivtool.acivtool import AciVTool
from argparse import RawTextHelpFormatter

if __name__ == "__main__":
    help_example = "example usage 1 (generate new serial numbers):\n" \
                   "\tpython new-vpodvm.py --vcenter 172.23.143.235 --vc-username admin --vc-password lab --host-name 172.23.143.129 --mgmt-pg 'VM Network' --infra-pg 'mininet/infra' --ovf-item vpod_77_4 --vpod-id 2  --auth-mode passphrase --auth-key 3NWG4NDP4DESTZL2" \
                   "\n\nexample usage 2 (use existing serial nubmers):\n" \
                   "\tpython new-vpodvm.py --vcenter 172.23.143.235 --vc-username admin --vc-password lab --host-name 172.23.143.129 --mgmt-pg 'VM Network' --infra-pg 'mininet/infra' --ovf-item vpod_77_4 --vpod-id 2 --auth-mode passphrase --auth-key 3NWG4NDP4DESTZL2 --vspine-serial 'SPINE201-SWJI' --vleaf-serial 'LEAF203-VIWE'" \
                   "\n\nexample usage 3:\n" \
                   "\tpython new-vpodvm.py --vcenter 172.23.143.235 --vc-username admin --vc-password lab --host-name 172.23.143.129 --mgmt-pg 'VM Network' --infra-pg 'mininet/infra' --ovf-item vpod_77_4 --vpod-id 2 --auth-mode passphrase --auth-key 3NWG4NDP4DESTZL2 --vspine-serial 'SPINE201-SWJI' --vleaf-serial 'LEAF203-VIWE' --library cisco-library --datastore datastore1 --vspine-ip 172.23.150.100 --vspine-netmask 255.255.255.0 --vspine-gateway 172.23.150.254 --vleaf-ip 172.23.150.101 --vleaf-netmask 255.255.255.0 --vleaf-gateway 172.23.150.254"

    parser = argparse.ArgumentParser(epilog=help_example, formatter_class=RawTextHelpFormatter)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    parser.add_argument("--vcenter",  help='vCenter IP / FQDN', required=True)
    parser.add_argument("--vc-username", type=str, help = 'vCenter username', required=True)
    parser.add_argument( "--vc-password", type =str, help='vCenter user password' , required=False)

    parser.add_argument("--host-name", "--hostName", type=str, help='Name of the Host', required=True)

    parser.add_argument("--mgmt-pg", type = str, help = 'Desired management port group. Format: \'Network name\' or \'DVS_name/Portgroup name\'', required=True)
    parser.add_argument("--infra-pg",  type = str, help = 'Infra port group. Format: \'Network name\' or \'DVS_name/Portgroup name\'', required=True)

    parser.add_argument("--ovf-item",  type = str, help = 'Name of the OVF Content Library Item to deploy', required=True)
    parser.add_argument("--vpod-id", type=str, help='vPOD ID', required=True)
    parser.add_argument("--auth-mode", type=str, help='Mode that will be used by the vPod Virtual Machine to authenticate to APIC. Supported values are \'passphrase\' or \'password\'', required=False)
    parser.add_argument("--auth-key", type=str, help='Authentication key (APIC admin password or APIC passphrase based on the value of --auth-mode)', required=False)

    parser.add_argument("--vspine-serial", type=str, help='vSpine Serial Number. If this parameter is not specfied, a serial number will be automatically generated', required=False)
    parser.add_argument("--vleaf-serial", type=str, help='vLeaf Serial Number. If this parameter is not specfied, a serial number will be automatically generated', required=False)

    parser.add_argument("--library", type=str, help='Name of the Content Library hosting the OvfItem',required=False)
    parser.add_argument("--datastore", type=str, help='Name of the datastore on which the VMs should be installed', required=False)

    parser.add_argument("--vspine-ip", type=str, help='vSpine Static Management IP address', required=False)
    parser.add_argument("--vspine-netmask", type=str, help='vSpine Static Management Network Mask', required=False)
    parser.add_argument("--vspine-gateway", type=str, help='vSpine Static Management Gateway', required=False)
    parser.add_argument("--vspine-nameserver", type=str, help='vSpine Static DNS server IP', required=False)

    parser.add_argument("--vleaf-ip", type=str, help='vLeaf Static Management IP address', required=False)
    parser.add_argument("--vleaf-netmask", type=str, help='vLeaf Static Management Network Mask', required=False)
    parser.add_argument("--vleaf-gateway", type=str, help='vLeaf Static Management Gateway', required=False)
    parser.add_argument("--vleaf-nameserver", type=str, help='vLeaf Static DNS server IP', required=False)

    args = parser.parse_args()

    vtool = AciVTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.vpod_new(host_name=args.host_name,
                   auth_mode=args.auth_mode, auth_key=args.auth_key,
                   datastore_name=args.datastore, infra_pg=args.infra_pg,
                   library_name=args.library, mgmt_name=args.mgmt_pg,
                   ovf_name=args.ovf_item, vleaf_gateway=args.vleaf_gateway,
                   vleaf_ip=args.vleaf_ip, vleaf_nameserver=args.vleaf_nameserver,
                   vleaf_netmask=args.vleaf_netmask, vleaf_serial_number=args.vleaf_serial,
                   vpod_id=args.vpod_id, vspine_gateway=args.vspine_gateway,
                   vspine_ip=args.vspine_ip, vspine_nameserver=args.vspine_nameserver,
                   vspine_netmask=args.vspine_netmask, vspine_serial_number=args.vspine_serial)