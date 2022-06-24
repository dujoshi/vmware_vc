################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems, Inc.                                       #
# All Rights Reserved.                                                         #
#                                                                              #
# Name: new-avevm.py                                                           #
# Purpose: Script to deploy a new Cisco AVE VM                                 #
#                                                                              #
################################################################################

import argparse
from lib.acivtool.acivtool import AciVTool
from argparse import RawTextHelpFormatter

def enterprise_mode(args):
    vtool = AciVTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.ave_new(host_name=args.host_name, domain_name=args.domain_name, ovf_name=args.ovf_item,
                  mgmt_name=args.mgmt_pg, infra_vlan=args.infra_vlan, apic_version=args.apic_version, admin_password=args.admin_password,
                  datastore_name=args.datastore, ip=args.ip, netmask=args.netmask, gateway=args.gateway, nameserver=args.nameserver,
                  library_name=args.library, ave_hostname=args.vm_hostname)


def cloud_mode(args):
    vtool = AciVTool(args.silent)
    vtool.vmware_set_auth(args.vcenter, args.vc_username, args.vc_password)
    vtool.ave_new(host_name=args.host_name, domain_name=args.domain_name, ovf_name=args.ovf_item,
                  mgmt_name=args.mgmt_pg, infra_vlan=args.infra_vlan, apic_version=args.apic_version, admin_password=args.admin_password,
                  datastore_name=args.datastore, ip=args.ip, netmask=args.netmask, gateway=args.gateway, nameserver=args.nameserver,
                  library_name=args.library, mode='cloud', vpod_id=args.vpod_id, vtor1_ip=args.vtor1_ip, vtor2_ip=args.vtor2_ip,
                  vtep_ip=args.vtep_ip, vtep_netmask=args.vtep_netmask, vtep_gateway=args.vtep_gateway, ave_hostname=args.vm_hostname)


if __name__ == "__main__":
    help_example = "example usage:\n" \
                   "\tenterprise mode:\n" \
                   "\t\tpython new-avevm.py --vcenter 172.31.100.10 --vc-username 'administrator@vsphere.local' --vc-password 'vcpassword' " \
                   "--host-name 172.31.100.12 --domain-name 'mininet' --mgmt-pg 'VM Network' --infra-vlan 10" \
                   " --ovf-item cisco-ave.ovf --datastore datastore01 --admin-password 'adminpassword' --apic-version '4.0(0.0)' --ip 172.31.100.11 " \
                   "--netmask 255.255.255.0 --gateway 172.31.100.1 --nameserver 172.23.140.25 Enterprise" \
                   "\n\n\tvPod mode:\n" \
                   "\t\tpython new-avevm.py --vcenter 172.31.100.10 --vc-username 'administrator@vsphere.local' --vc-password 'vcpassword' " \
                   "--host-name 172.31.100.12 --domain-name 'mininet' --mgmt-pg 'VM Network' --infra-vlan 10" \
                   " --ovf-item cisco-ave.ovf --datastore datastore01 --admin-password 'adminpassword' --apic-version '4.0(0.0)' --ip 172.31.100.11 " \
                   "--netmask 255.255.255.0 --gateway 172.31.100.1 --nameserver 172.23.140.25 vPod --vpod-id 2"

    parser = argparse.ArgumentParser(epilog=help_example, formatter_class=RawTextHelpFormatter)
    parser.add_argument("--silent", action='store_true', help='Do not show stdout ouput', required=False)
    parser.add_argument("--vcenter", "--vcHost",  help='vCenter IP/FQDN', required=True)
    parser.add_argument("--vc-username", "--vcUser", type=str, help = 'vCenter Username', required=True)
    parser.add_argument("--vc-password", "--vcPwd", type =str, help='vCenter Password', required=False)
    parser.add_argument("--host-name", "--hostName",  type = str, help = 'Name of the Host', required=True)
    parser.add_argument("--domain-name", "--domainName", type=str, help = 'Name of the domain DVS', required=True)
    parser.add_argument("--mgmt-pg", "--mgmtPortgroupName",  type = str, help = 'Desired management port group. Format: "Network name" or "DVS_name/Portgroup name"', required=True)
    parser.add_argument("--admin-password", "--adminPassword",  type = str, help = 'The password to set for the "admin" user of the VM', required=False)
    parser.add_argument("--infra-vlan", "--infraVlan",  type = int, help = 'The APIC Infra Vlan', required=True)
    parser.add_argument("--ovf-item", "--ovfItem",  type = str, help = 'Name of the OVF Content Library Item to deploy', required=True)
    parser.add_argument("--library", type=str, help='Name of the Content Library hosting the OvfItem',required=False)
    parser.add_argument("--datastore", type=str, help='Name of the datastore on which the AVE VM should be installed', required=False)
    parser.add_argument("--ip", type=str, help='Static Management IP address', required=False)
    parser.add_argument("--netmask", type=str, help='Static Management Network Mask', required=False)
    parser.add_argument("--gateway", type=str, help='Static Management Gateway', required=False)
    parser.add_argument("--nameserver", type=str, help='Static DNS server IP', required=False)
    parser.add_argument("--vm-hostname", "--vmHostname", type=str, help='Hostname to be used for the AVE VM', required=False)
    parser.add_argument("--apic-version", "--apicVersion", type=str, help='Version of APIC ex: 3.1(0.158a)', required=True)
    parser.set_defaults(func=enterprise_mode)


    subparsers = parser.add_subparsers(help='vPod Mode Ave')
    cloud_parser = subparsers.add_parser("vPod")
    ent_parser = subparsers.add_parser("Enterprise")
    cloud_parser.add_argument("--vpod-id", type=str, help='vPOD ID', required=True)
    cloud_parser.add_argument("--vtor1-ip", type=str, help='vTor 1 Management IP address', required=False)
    cloud_parser.add_argument("--vtor2-ip", type=str, help='vTor 2 Management IP address', required=False)
    cloud_parser.add_argument("--vtep-ip", type=str, help='vTep Static IP address', required=False)
    cloud_parser.add_argument("--vtep-netmask", type=str, help='vTep Network Mask', required=False)
    cloud_parser.add_argument("--vtep-gateway", type=str, help='vTep Gateway', required=False)
    cloud_parser.set_defaults(func=cloud_mode)

    args = parser.parse_args()
    args.func(args)
